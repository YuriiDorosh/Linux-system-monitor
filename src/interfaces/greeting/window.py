import os
import json
import customtkinter as Ctk
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
from .. import console, gui


class MainWindow(Ctk.CTk):
    """
    Represents the main window of the Linux System Monitor application.

    Attributes:
    - img_folder (str): The path to the folder containing image resources.
    - logo (CTkImage): An instance of the CTkImage class representing the application logo.
    - logo_label (CTkLabel): A label to display the application logo.
    - btn_gui (CTkButton): A button to open the GUI Monitor.
    - btn_cons (CTkButton): A button to open the Console Monitor.
    - settings_label (CTkLabel): A label for the settings section.
    - fps_label (CTkLabel): A label for the Frames per Second (fps) setting.
    - fps_combobox (ttk.Combobox): A combobox to select the fps value.
    - video_format_label (CTkLabel): A label for the Video Format setting.
    - video_format_combobox (ttk.Combobox): A combobox to select the video format.
    - monitor_resolution_label (CTkLabel): A label for the Monitor Resolution setting.
    - monitor_resolution_combobox (ttk.Combobox): A combobox to select the monitor resolution.
    - btn_apply (CTkButton): A button to apply the settings.

    Methods:
    - __init__(): Initializes the MainWindow instance and sets up the GUI components.
    - start_gui(): Starts the GUI Monitor with the selected settings.
    - start_console(): Starts the Console Monitor.
    - save_changing(): Placeholder method for saving changes.
    - refresh_gui(): Placeholder method for refreshing the GUI.
    - apply_settings(): Applies the selected settings and saves them to a JSON file.
    - run(): Runs the main event loop for the GUI.
    """

    def __init__(self):
        super().__init__()

        self.img_folder = os.path.abspath("../src/images/project/for-greeting-window")

        self.geometry("600x800")
        self.title("Linux System Monitor")
        self.resizable(False, False)

        img_path = os.path.join(self.img_folder, "sys.png")
        self.logo = Ctk.CTkImage(dark_image=Image.open(img_path), size=(600, 300))
        self.logo_label = Ctk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, pady=20)

        self.btn_gui = Ctk.CTkButton(
            master=self,
            text="Open GUI Monitor",
            width=30,
            height=2,
            command=self.start_gui,
        )
        self.btn_gui.grid(row=1, column=0, padx=10, pady=10)

        self.btn_cons = Ctk.CTkButton(
            master=self,
            text="Open Console Monitor",
            width=30,
            height=2,
            command=self.start_console,
        )
        self.btn_cons.grid(row=2, column=0, padx=10, pady=10)

        self.settings_label = Ctk.CTkLabel(
            master=self, text="Settings for GUI Monitor (screen recording)"
        )
        self.settings_label.grid(row=3, column=0, padx=10, pady=10)

        self.fps_label = Ctk.CTkLabel(master=self, text="Frames per Second (fps):")
        self.fps_label.grid(row=4, column=0, padx=10, pady=10)
        self.fps_combobox = ttk.Combobox(self, values=[15, 30, 60, 120])
        self.fps_combobox.current(1)  # Set default value to 30
        self.fps_combobox.grid(row=5, column=0, padx=10, pady=10)

        self.video_format_label = Ctk.CTkLabel(master=self, text="Video Format:")
        self.video_format_label.grid(row=6, column=0, padx=10, pady=10)
        self.video_format_combobox = ttk.Combobox(
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
        )
        self.video_format_combobox.current(0)
        self.video_format_combobox.grid(row=7, column=0, padx=10, pady=10)

        self.monitor_resolution_label = Ctk.CTkLabel(
            master=self, text="Monitor Resolution:"
        )
        self.monitor_resolution_label.grid(row=8, column=0, padx=10, pady=10)
        self.monitor_resolution_combobox = ttk.Combobox(
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
        )
        self.monitor_resolution_combobox.current(4)
        self.monitor_resolution_combobox.grid(row=9, column=0, padx=10, pady=10)

        self.btn_apply = Ctk.CTkButton(
            master=self, text="Apply", width=30, command=self.apply_settings
        )
        self.btn_apply.grid(row=10, column=0, padx=10, pady=10)

    def start_gui(self):
        """
        Starts the GUI Monitor with the selected settings.
        """
        gui_interface = gui.gui_interface.GuiInterface()
        fps = int(self.fps_combobox.get())
        video_format = self.video_format_combobox.get()
        monitor_resolution = self.monitor_resolution_combobox.get()

        if (
            fps not in [15, 30, 60, 120]
            or video_format
            not in [
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
            ]
            or monitor_resolution
            not in [
                "640x480",
                "720x480",
                "720x576",
                "1280x720",
                "1920x1080",
                "3840x2160",
                "4096x2160",
                "5120x2880",
                "7680x4320",
            ]
        ):
            messagebox.showerror(
                "Error",
                "Invalid settings! Please choose valid FPS, Video Format, and Monitor Resolution.",
            )
        else:
            settings = {
                "fps": fps,
                "video_format": video_format,
                "monitor_resolution": monitor_resolution,
            }
            settings_file_path = os.path.abspath("../src/settings.json")
            with open(settings_file_path, "w") as file:
                json.dump(settings, file)

            self.destroy()
            gui_interface.run()

    def start_console(self):
        """
        Starts the Console Monitor.
        """
        console_interface = console.console_interface.ConsoleInterface()
        self.destroy()
        console_interface.run()

    def apply_settings(self):
        """
        Applies the selected settings and saves them to a JSON file.
        """
        fps = int(self.fps_combobox.get())
        video_format = self.video_format_combobox.get()
        monitor_resolution = self.monitor_resolution_combobox.get()

        if (
            fps not in [15, 30, 60, 120]
            or video_format
            not in [
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
            ]
            or monitor_resolution
            not in [
                "640x480",
                "720x480",
                "720x576",
                "1280x720",
                "1920x1080",
                "3840x2160",
                "4096x2160",
                "5120x2880",
                "7680x4320",
            ]
        ):
            messagebox.showerror(
                "Error",
                "Invalid settings! Please choose valid FPS, Video Format, and Monitor Resolution.",
            )
        else:
            settings = {
                "fps": fps,
                "video_format": video_format,
                "monitor_resolution": monitor_resolution,
            }
            settings_file_path = os.path.abspath("../src/settings.json")
            with open(settings_file_path, "w") as file:
                json.dump(settings, file)

            messagebox.showinfo(
                "Settings",
                f"FPS: {fps}, Video Format: {video_format}, Monitor Resolution: {monitor_resolution}",
            )

    def run(self):
        """
        Runs the main event loop for the GUI.
        """
        self.mainloop()


if __name__ == "__main__":
    window = MainWindow()
    window.run()
