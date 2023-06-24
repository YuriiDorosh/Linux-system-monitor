import curses
from system_info import SystemInfo


class ConsoleInterface:
    def __init__(self):
        self.system_info = SystemInfo()

    def update_console(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")
        cpu_load = self.system_info.get_cpu_load()
        memory_usage = self.system_info.get_memory_usage()
        disk_usage = self.system_info.get_disk_usage()
        gpu_usage = self.system_info.get_gpu_usage()

        progress_bars = [f"CPU{i+1}: {load}%" for i, load in enumerate(cpu_load)] + [
            f"Memory: {memory_usage}%",
            f"Disk: {disk_usage}%",
            f"GPU: {gpu_usage}%",
        ]

        disk_info = f"Disk Free Space: {self.system_info.get_disk_free_space():.2f} GB"

        for i, progress_bar in enumerate(progress_bars):
            stdscr.addstr(i + 2, 0, progress_bar)

        stdscr.addstr(len(progress_bars) + 2, 0, disk_info)

        stdscr.refresh()

    def run(self):
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.nodelay(True)

        while True:
            self.update_console(stdscr)

            key = stdscr.getch()
            if key == ord("q"):
                break

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
