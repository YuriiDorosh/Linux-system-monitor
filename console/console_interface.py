import curses

from system.system_interface import SystemInterface


class ConsoleInterface:
    def __init__(self):
        self.system_interface = SystemInterface()

    def update_console(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")

        progress_bars = self.system_interface.get_progress_bars()
        disk_info = self.system_interface.get_disk_info()

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


if __name__ == "__main__":
    interface = ConsoleInterface()
    interface.run()
