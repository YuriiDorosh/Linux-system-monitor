import tkinter as tk
from tkinter import ttk, messagebox
import json
import settings


class SettingsWindow(tk.Tk):
    """
    This class represents the settings_interface window.
    It is responsible for providing the UI for user settings_interface
    and saving them into a JSON file. It is derived from the tk.Tk class, which represents a tkinter toplevel widget,
    essentially it is the main window of an application.
    """

    def __init__(self) -> None:
        super().__init__()

        self.title("Settings")

        save_button = ttk.Button(self, text="Save", command=self.save_settings)
        save_button.pack()

        # Create and initialize a DoubleVar for CPU percent interval
        self.cpu_percent_interval_var = tk.DoubleVar(value=settings.SystemInfo.cpu_percent_interval)
        ttk.Label(self, text="CPU Percent Interval:").pack()
        ttk.Spinbox(
            self,
            from_=0.01,
            to=5.0,
            increment=0.01,
            textvariable=self.cpu_percent_interval_var,
        ).pack()

        # Create and initialize a StringVar for Video extension
        self.video_extension_var = tk.StringVar(value=settings.ScreenRecording.video_extension)
        ttk.Label(self, text="Video Extension:").pack()
        ttk.Combobox(
            self,
            values=[
                "mp4",
                "avi",
                "mkv",
                "mov",
                "wmv",
                "flv",
                "webm",
                "mpeg",
                "3gp",
                "ts",
            ],
            textvariable=self.video_extension_var,
        ).pack()

        # Create and initialize a StringVar for Frame rate
        self.frame_rate_var = tk.StringVar(value=settings.ScreenRecording.frame_rate)
        ttk.Label(self, text="Frame Rate (FPS):").pack()
        ttk.Combobox(
            self,
            values=[
                "15",
                "24",
                "30",
                "60",
            ],
            textvariable=self.frame_rate_var,
        ).pack()

        # Create and initialize a StringVar for Monitor resolution
        self.monitor_resolution_var = tk.StringVar(value=settings.ScreenRecording.monitor_resolution)
        ttk.Label(self, text="Monitor Resolution:").pack()
        ttk.Combobox(
            self,
            values=[
                "640x480",
                "720x480",
                "720x576",
                "1280x720",
                "1920x1080",
                "3840x2160",
                "4096x2160",
                "5120x2880",
                "7680x4320",
            ],
            textvariable=self.monitor_resolution_var,
        ).pack()

        # Create and initialize StringVars for KeyBindings
        self.topmost_var = tk.StringVar(value=settings.KeyBindings.topmost)
        self.start_recording_var = tk.StringVar(value=settings.KeyBindings.start_recording)
        self.minimalize_var = tk.StringVar(value=settings.KeyBindings.minimalize)
        self.screenshot_var = tk.StringVar(value=settings.KeyBindings.screenshot)

        self.key_bindings_list = [
            "<F1>",
            "<F2>",
            "<Ctrl-Alt-Del>",
            "<Shift-Tab>",
            "<Ctrl-C>",
            "<Control-t>",
            "<Control-r>",
            "<Control-m>",
            "<Control-s>",
            # Add more options here...
        ]

        ttk.Label(self, text="Topmost Keybinding:").pack()
        ttk.Combobox(self, values=self.key_bindings_list, textvariable=self.topmost_var).pack()

        ttk.Label(self, text="Start Recording Keybinding:").pack()
        ttk.Combobox(self, values=self.key_bindings_list, textvariable=self.start_recording_var).pack()

        ttk.Label(self, text="Minimalize Keybinding:").pack()
        ttk.Combobox(self, values=self.key_bindings_list, textvariable=self.minimalize_var).pack()

        ttk.Label(self, text="Screenshot Keybinding:").pack()
        ttk.Combobox(self, values=self.key_bindings_list, textvariable=self.screenshot_var).pack()

    def save_settings(self) -> None:
        """
        This method saves the current settings_interface into a JSON file.
        It's called when the user clicks on the 'Apply' button.
        """
        # Validate FPS
        fps = int(self.frame_rate_var.get())
        if fps not in [15, 24, 30, 60]:
            messagebox.showerror("Error", "Invalid FPS value!")
            return

        # Validate Video Format
        video_format = self.video_extension_var.get()
        if video_format not in [
            "mp4",
            "avi",
            "mkv",
            "mov",
            "wmv",
            "flv",
            "webm",
            "mpeg",
            "3gp",
            "ts",
        ]:
            messagebox.showerror("Error", "Invalid video format!")
            return

        # Validate Monitor Resolution
        monitor_resolution = self.monitor_resolution_var.get()
        if monitor_resolution not in [
            "640x480",
            "720x480",
            "720x576",
            "1280x720",
            "1920x1080",
            "3840x2160",
            "4096x2160",
            "5120x2880",
            "7680x4320",
        ]:
            messagebox.showerror("Error", "Invalid monitor resolution!")
            return

        # Validate keybindings
        if not self.is_valid_binding(self.topmost_var.get()):
            messagebox.showerror("Error", "Invalid 'Topmost' keybinding!")
            return

        if not self.is_valid_binding(self.start_recording_var.get()):
            messagebox.showerror("Error", "Invalid 'Start Recording' keybinding!")
            return

        if not self.is_valid_binding(self.minimalize_var.get()):
            messagebox.showerror("Error", "Invalid 'Minimalize' keybinding!")
            return

        if not self.is_valid_binding(self.screenshot_var.get()):
            messagebox.showerror("Error", "Invalid 'Screenshot' keybinding!")
            return

        # If all validations pass, save to JSON
        with open(settings.settings_file_path, "w") as file:
            json.dump(
                {
                    "cpu_percent_interval": float(self.cpu_percent_interval_var.get()),
                    "video_format": video_format,
                    "fps": fps,
                    "monitor_resolution": monitor_resolution,
                    "topmost": self.topmost_var.get(),
                    "start_recording": self.start_recording_var.get(),
                    "minimalize": self.minimalize_var.get(),
                    "screenshot": self.screenshot_var.get(),
                },
                file,
            )

    @staticmethod
    def is_valid_binding(binding: str) -> bool:
        """
        Check if the binding is valid. It must be a single character or a special key combination.
        """
        # Add your specific constraints here, e.g. allowed special keys
        special_keys = [
            "<F1>",
            "<F2>",
            "<Ctrl-Alt-Del>",
            "<Shift-Tab>",
            "<Ctrl-C>",
            "<Control-t>",
            "<Control-r>",
            "<Control-m>",
            "<Control-s>",
        ]
        # Check if binding is a single character or a special key combination
        return len(binding) == 1 or binding in special_keys

    def run(self) -> None:
        self.mainloop()


if __name__ == "__main__":
    # Create an instance of SettingsWindow and start the
    window = SettingsWindow()
    window.mainloop()
