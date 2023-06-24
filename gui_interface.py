import tkinter as tk
import subprocess
import datetime
import os
import errno
from system_interface import SystemInterface


class GuiInterface:
    def __init__(self):
        self.system_interface = SystemInterface()
        self.root = tk.Tk()
        self.root.title("System Monitor")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, font=("Courier", 12), justify=tk.LEFT)
        self.label.pack(padx=10, pady=10)

        self.topmost = False

        self.button = tk.Button(
            self.root, text="Toggle Topmost", command=self.toggle_topmost
        )
        self.button.pack(pady=5)

        self.record_button = tk.Button(
            self.root, text="Record Screen", command=self.toggle_recording
        )
        self.record_button.pack(pady=5)

        self.recording = False
        self.process = None

    def toggle_topmost(self):
        self.topmost = not self.topmost

        if self.topmost:
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.record_button.config(text="Stop Recording")

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"output_{timestamp}.mp4"

        current_path = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_path, "recordings", filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        print("Starting recording...")
        print(f"Output Path: {output_path}")

        display_num = os.environ.get("DISPLAY", ":0.0")
        self.process = subprocess.Popen(
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

    def stop_recording(self):
        self.recording = False
        self.record_button.config(text="Record Screen")

        try:
            self.process.stdin.write("q")
            self.process.stdin.flush()
            self.process.communicate()

        except (BrokenPipeError, OSError) as e:
            if e.errno != errno.EPIPE:
                raise

    def update_gui(self):
        progress_bars = self.system_interface.get_progress_bars()
        disk_info = self.system_interface.get_disk_info()

        text = "\n".join(progress_bars) + "\n" + disk_info
        self.label.config(text=text)

        self.root.after(1000, self.update_gui)

    def run(self):
        self.update_gui()
        self.root.mainloop()


if __name__ == "__main__":
    interface = GuiInterface()
    interface.run()
