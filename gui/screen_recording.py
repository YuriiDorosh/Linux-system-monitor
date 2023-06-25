import subprocess
import datetime
import os
import errno

import settings

process = None


def record():
    """
    Starts a screen recording using FFmpeg.

    This function initializes a screen recording process using FFmpeg with the specified settings.
    The output video file will be saved with a timestamped filename in the configured output directory.
    """
    global process

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{timestamp}.{settings.ScreenRecording.video_extension}"

    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_path)

    output_path = os.path.join(parent_path, "recordings", filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("Starting recording...")
    print(f"Output Path: {output_path}")

    display_num = os.environ.get("DISPLAY", ":0.0")
    process = subprocess.Popen(
        [
            "ffmpeg",
            "-video_size",
            settings.ScreenRecording.monitor_resolution,
            "-framerate",
            str(settings.ScreenRecording.frame_rate),
            "-f",
            "x11grab",
            "-i",
            display_num,
            output_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        encoding="utf-8",
    )
    print("Recording process started.")


def stop_recording():
    """
    Stops the screen recording process.

    This function stops the screen recording process by sending the 'q' command to the FFmpeg process.
    It flushes the input stream, communicates with the process, and terminates it gracefully.
    """
    global process
    try:
        process.stdin.write("q")
        process.stdin.flush()
        process.communicate()
        print("Stop Recording")

    except (BrokenPipeError, OSError) as e:
        if e.errno != errno.EPIPE:
            raise
