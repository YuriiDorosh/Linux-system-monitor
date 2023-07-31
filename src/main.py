import sys
import platform
import os


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


def get_help_text():
    """
    Retrieves the content of the help file.

    This function reads the 'help.txt' file located in the project's top-level directory (beside 'src/').
    If the file exists, its content is returned; otherwise, a message indicating that the file is not found is returned.

    Returns:
        str: The content of the 'help.txt' file, or a message stating that the file is not found.
    """
    help_file_path = os.path.join(os.path.dirname(__file__), "..", "help.txt")
    if os.path.isfile(help_file_path):
        with open(help_file_path, "r") as file:
            return file.read()
    else:
        return "Help file not found."


def main():
    """
    Main function to run the program.

    It checks the operating system and the presence of an NVIDIA graphics card,
    then launches the appropriate interface or displays relevant messages.

    This program supports running in Linux environments with NVIDIA graphics cards.

    Usage:
        To run the GUI version: python(3) __main__.py --gui or python(3) __main__.py -g
        To run the console version: python(3) __main__.py --console or python(3) __main__.py -c
        To display this help message: python(3) __main__.py --help or python(3) __main__.py -h
    """
    if "--help" in sys.argv or "-h" in sys.argv:
        print(main.__doc__)
        help_text = get_help_text()
        print(f"\n{'*' * 50}\n" "\nAdditional Help Text:" "\n")
        print(help_text)
        sys.exit(0)

    if platform.system() == "Windows":
        print("This program is intended for Linux and is not supported on Windows.")
        sys.exit(1)
    else:
        from .interfaces import gui, console, greeting

        if not check_nvidia_gpu():
            print(
                "This program works only with NVIDIA video cards."
                "\nIf you have an NVIDIA graphics card, check if the drivers are installed."
                "\nTry(Ubuntu): sudo ubuntu-drivers autoinstall"
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
