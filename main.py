import sys

import gui
import console


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        gui_interface = gui.gui_interface.GuiInterface()
        gui_interface.run()
    else:
        console_interface = console.console_interface.ConsoleInterface()
        console_interface.run()


if __name__ == "__main__":
    main()
