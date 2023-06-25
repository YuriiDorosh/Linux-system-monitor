import subprocess
import datetime
import os
import errno


process = None


def record():
    global process

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{timestamp}.mp4"

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
            "1920x1080",
            "-framerate",
            "30",
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
    global process
    try:
        process.stdin.write("q")
        process.stdin.flush()
        process.communicate()
        print("Stop Recording")

    except (BrokenPipeError, OSError) as e:
        if e.errno != errno.EPIPE:
            raise
