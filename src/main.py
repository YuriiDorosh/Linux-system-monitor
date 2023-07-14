import sys

from interfaces import gui, console, greeting


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--gui" or sys.argv[1] == "-g":
            gui_interface = gui.gui_interface.GuiInterface()
            gui_interface.run()
        elif sys.argv[1] == "--console" or sys.argv[1] == "-c":
            console_interface = console.console_interface.ConsoleInterface()
            console_interface.run()
        else:
            greeting_window = greeting.window.MainWindow()
            greeting_window.run()
    else:
        greeting_window = greeting.window.MainWindow()
        greeting_window.run()


if __name__ == "__main__":
    main()
