import os

import customtkinter as Ctk
from PIL import Image

from .. import console, gui, settings_interface


class MainWindow(Ctk.CTk):
    """
    A class that represents the main window of the application.

    Inherits from Ctk.CTk which is a tkinter wrapper.

    Attributes:
        img_folder (str): The absolute path of the directory where images are stored.
        logo (Ctk.CTkImage): An image object representing the logo of the application.
        logo_label (Ctk.CTkLabel): The label on which the logo is displayed.
        btn_gui (Ctk.CTkButton): Button to launch the GUI monitor.
        btn_cons (Ctk.CTkButton): Button to launch the console monitor.
        btn_settings (Ctk.CTkButton): Button to open the settings.

    """

    def __init__(self):
        """Initializes MainWindow with a set layout and features."""
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

        self.btn_settings = Ctk.CTkButton(
            master=self,
            text="Open Settings",
            width=30,
            height=2,
            command=self.open_settings,
        )
        self.btn_settings.grid(row=3, column=0, padx=10, pady=10)

    def start_gui(self):
        """Starts the GUI monitor and closes the current window."""
        gui_interface = gui.gui_interface.GuiInterface()
        gui_interface.run()
        self.withdraw()
        self.destroy()

    def start_console(self):
        """Starts the console monitor and closes the current window."""
        console_interface = console.console_interface.ConsoleInterface()
        self.destroy()
        console_interface.run()

    def open_settings(self):
        """Opens the settings window and minimizes the current window."""
        settings_window = settings_interface.settings_window.SettingsWindow()
        self.withdraw()
        self.deiconify()

    def run(self):
        """Runs the main loop of the tkinter interface."""
        self.mainloop()


if __name__ == "__main__":
    window = MainWindow()
    window.run()
