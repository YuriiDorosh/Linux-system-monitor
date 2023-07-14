import os

import customtkinter as Ctk
from PIL import Image

from .. import console, gui


class MainWindow(Ctk.CTk):
    def __init__(self):
        super().__init__()

        img_folder = os.path.abspath("../src/images/project/for-greeting-window")

        self.geometry("600x800")
        self.title("Linux System Monitor")
        self.resizable(False, False)

        img_path = os.path.join(img_folder, "sys.png")
        self.logo = Ctk.CTkImage(dark_image=Image.open(img_path), size=(600, 300))
        self.logo_label = Ctk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.btn_gui = Ctk.CTkButton(master=self, text="Open GUI Monitor", width=200,
                                     command=self.start_gui)
        self.btn_gui.grid(row=1, column=0, padx=10, pady=10)

        self.btn_cons = Ctk.CTkButton(master=self, text="Open Console Monitor", width=200,
                                      command=self.start_console)
        self.btn_cons.grid(row=2, column=0, padx=10, pady=10)


    def start_gui(self):
        gui_interface = gui.gui_interface.GuiInterface()
        self.destroy()
        gui_interface.run()
    def start_console(self):
        console_interface = console.console_interface.ConsoleInterface()
        self.destroy()
        console_interface.run()



    def save_changing(self):
        pass

    def refresh_gui(self):
        pass

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
