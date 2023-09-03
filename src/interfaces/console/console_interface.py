import curses

from system.system_interface import SystemInterface


class ConsoleInterface:
    """
    A class representing a console interface for displaying system information.

    The ConsoleInterface class utilizes the curses library to create a console-based interface
    for displaying system information such as progress bars and disk information. It interacts with
    the SystemInterface class to retrieve the necessary information.

    Usage:
        Create an instance of the ConsoleInterface class and call the `run()` method to start the
        console interface. Press 'q' to quit the interface.

    Example:
        if __name__ == "__main__":
            interface = ConsoleInterface()
            interface.run()
    """

    def __init__(self) -> None:
        """
        Initialize the ConsoleInterface object.

        This method initializes the ConsoleInterface object by creating an instance of the
        SystemInterface class to interact with the system and retrieve system information.
        """
        self.system_interface = SystemInterface()

    def update_console(self, stdscr: "curses.window") -> None:
        """
        Update the console interface with system information.

        This method updates the console interface by clearing the screen, displaying a message,
        retrieving progress bars and disk information from the SystemInterface object, and
        refreshing the screen.

        Args:
            stdscr (curses window): The curses window object representing the console screen.
        """
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")

        progress_bars = self.system_interface.get_progress_bars()

        for i, progress_bar in enumerate(progress_bars):
            stdscr.addstr(i + 2, 0, progress_bar)

        stdscr.addstr(str(len(progress_bars) + 2), 0)

        stdscr.refresh()

    def run(self) -> None:
        """
        Run the console interface.

        This method starts the console interface by initializing the curses library, setting up the
        console screen, and entering the main loop. The console interface is continuously updated
        until the user presses 'q' to quit.
        """
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
