import subprocess
import datetime
import os
import errno
import logging
import settings
from typing import List

logging.basicConfig(level=logging.INFO)


class ScreenRecorder:
    """
    A class that provides methods to start and stop a screen recording.

    Attributes:
        process (subprocess.Popen): The process running the screen recording.

    Methods:
        start() -> None: Starts the screen recording.
        stop() -> None: Stops the screen recording.
    """

    def __init__(self) -> None:
        self.process = None

    def _get_command(self, display_num: str, output_path: str) -> List[str]:
        """Return the command to start the recording process."""
        return [
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
        ]

    def start(self) -> None:
        """
        Starts the screen recording and saves the output to a video file.
        """
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"output_{timestamp}.{settings.ScreenRecording.video_extension}"

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(project_root, "..", "recordings", filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        logging.info("Starting recording...")
        logging.info(f"Output Path: {output_path}")

        display_num = os.environ.get("DISPLAY", ":0.0")
        command = self._get_command(display_num, output_path)
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            encoding="utf-8",
        )
        logging.info("Recording process started.")

    def stop(self) -> None:
        """
        Stops the screen recording.
        """
        try:
            if self.process:
                self.process.stdin.write("q")
                self.process.stdin.flush()
                self.process.communicate()
            logging.info("Stop Recording")
        except (BrokenPipeError, OSError) as e:
            if e.errno != errno.EPIPE:
                raise
        finally:
            self.process = None
