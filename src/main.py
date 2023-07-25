import sys
import platform


def check_nvidia_gpu():
    import pynvml

    """
    Checks the presence of an NVIDIA graphics card on the system.

    This function uses the pynvml library to check for the presence of NVIDIA GPUs on the system.

    Returns:
        bool: True if an NVIDIA graphics card is present, otherwise False.
    """
    try:
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()
        pynvml.nvmlShutdown()
        return device_count > 0
    except pynvml.NVMLError as err:
        print(f"NVIDIA video card verification error: {err}\n")
        return False


def main():
    """
    Main function to run the program.

    It checks the operating system and the presence of an NVIDIA graphics card,
    then launches the appropriate interface or displays relevant messages.

    This program supports running in Linux environments with NVIDIA graphics cards.

    Usage:
        To run the GUI version: python main.py --gui
        To run the console version: python main.py --console

    """
    if platform.system() == "Windows":
        print("This program is intended for Linux and is not supported on Windows.")
        sys.exit(1)
    else:
        from interfaces import gui, console, greeting

        if not check_nvidia_gpu():
            print(
                "This program works only with NVIDIA video cards."
                "\nIf you have an NVIDIA graphics card, check if the drivers are installed."
            )
            sys.exit(1)
        else:
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


if __name__ == "__main__":
    main()
