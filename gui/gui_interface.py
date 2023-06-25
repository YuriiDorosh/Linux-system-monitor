import tkinter as tk


from .screen_recording import record, stop_recording

from system.system_interface import SystemInterface, ExtendedSystemInterface


class GuiInterface:
    def __init__(self):
        self.system_interface = SystemInterface()
        self.extended_system_interface = ExtendedSystemInterface()
        self.root = tk.Tk()
        self.root.title("System Monitor")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, font=("Courier", 12), justify=tk.LEFT)
        self.label.pack(padx=10, pady=10)

        self.topmost = False

        self.screen_label = "Rec/Stop Rec"
        self.recording = False

        self.minimalize_label = "Min/Max Win"
        self.minimalize = False

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.tools_menu = tk.Menu(self.menu, tearoff=False)
        self.tools_menu.add_command(label="Toggle Topmost", command=self.toggle_topmost)
        self.tools_menu.add_command(
            label=self.screen_label, command=self.toggle_recording
        )
        self.tools_menu.add_command(
            label=self.minimalize_label, command=self.minimalize_window
        )
        self.menu.add_cascade(label="Tools", menu=self.tools_menu)

    def toggle_topmost(self):
        self.topmost = not self.topmost

        if self.topmost:
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)

    def minimalize_window(self):
        if self.minimalize:
            self.minimalize = False
        else:
            self.minimalize = True

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        record()

    def stop_recording(self):
        self.recording = False
        stop_recording()

    def update_gui(self):
        if self.minimalize:
            cpu = self.extended_system_interface.get_average_cpu_load()
            gpu = self.extended_system_interface.get_gpu_usage_percentage()
            text = cpu + "\n" + gpu
            self.label.config(text=text)
            self.root.after(1000, self.update_gui)
        else:
            progress_bars = self.system_interface.get_progress_bars()
            disk_info = self.system_interface.get_disk_info()

            text = "\n".join(progress_bars) + "\n" + disk_info
            self.label.config(text=text)

            self.root.after(1000, self.update_gui)

    def show_all_buttons(self):
        if not hasattr(self, "button_frame"):
            self.button_frame = tk.Frame(self.root)
            self.button_frame.pack()

            self.buttons = [
                self.button,
                self.record_button,
                self.minimalize_button,
            ]
            for button in self.buttons:
                button.pack(side="top", padx=10, pady=5, fill="x")

            self.button_frame.pack_propagate(0)
        else:
            for button in self.buttons:
                button.pack_forget()
            self.button_frame.destroy()
            del self.button_frame

    def run(self):
        self.update_gui()
        self.root.mainloop()


if __name__ == "__main__":
    interface = GuiInterface()
    interface.run()
