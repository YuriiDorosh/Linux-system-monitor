import sys


from interfaces import gui, console


def main():
    if sys.argv[1] == "--gui" or sys.argv[1] == "-g":
        gui_interface = gui.gui_interface.GuiInterface()
        gui_interface.run()
    elif sys.argv[1] == "--console" or sys.argv[1] == "-c":
        console_interface = console.console_interface.ConsoleInterface()
        console_interface.run()
    else:
        pass


if __name__ == "__main__":
    main()
