import subprocess
import datetime
import os
import errno
import logging
import settings

logging.basicConfig(level=logging.INFO)


class ScreenRecorder:
    def __init__(self):
        self.process = None

    def _get_command(self, display_num, output_path):
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

    def start(self):
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

    def stop(self):
        """Stop the recording process."""
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
