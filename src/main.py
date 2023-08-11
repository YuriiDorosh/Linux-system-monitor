import sys
import platform
import os

import data_storage
from system.checkers import nvidia_checker
from interfaces import settings_interface
from interfaces import gui as gui_interface
from interfaces import console as console_interface
from interfaces import greeting as greeting_interface
from args import HELP_ARGS, GUI_ARGS, CONSOLE_ARGS, SETTINGS_ARGS
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def json_status() -> bool:
    """
    Asks the user whether to continue or exit the program.

    Continuation options are 'C' or 'continue', and exit options are 'E' or 'exit'.
    The check is case-insensitive.

    Returns:
        bool: True if the user chooses to continue, False if the user chooses to exit.
    """
    check_result = data_storage.settings.settings_analyzer.check_settings_file()
    logging.debug("Settings file status: %s", check_result)

    if check_result.status == "corrupt":
        print("Settings file was corrupted and restored to default values.")
        return True

    elif check_result.status == "default":
        while True:
            user_input = input(
                "Default settings detected. Would you like to change them? (Y)es/(N)o: "
            )
            if user_input.lower() in ["y", "yes"]:
                settings_win = settings_interface.settings_window.SettingsWindow()
                settings_win.run()
                return True
            elif user_input.lower() in ["n", "no"]:
                return True
            else:
                print(
                    "\nPlease, write 'Y' or 'yes' if you want to open the settings\n"
                    "and 'N' or 'no' to cancel the action.\n"
                )
    else:
        return True


def ask_user_to_continue() -> bool:
    """
    Asks the user whether to continue or exit the program.

    Returns:
        bool: True if the user chooses to continue, False if the user chooses to exit.
    """
    while True:
        user_input = input("(C)ontinue/(E)xit: ")
        if user_input.lower() == "c" or user_input.lower() == "continue":
            return True
        if user_input.lower() == "e" or user_input.lower() == "exit":
            return False
        else:
            print(
                "\nPlease, write 'C' or 'continue' if you want to run the program\n"
                "and 'E' or 'exit' to cancel the action.\n"
            )


def get_help_text() -> str:
    """
    Retrieves the content of the help file.

    This function reads the 'help.txt' file located in the project's top-level directory (beside 'src/').
    If the file exists, its content is returned; otherwise, a message indicating that the file is not found is returned.

    Returns:
        str: The content of the 'help.txt' file, or a message stating that the file is not found.
    """
    help_file_path: str = os.path.join(os.path.dirname(__file__), "..", "help.txt")
    if os.path.isfile(help_file_path):
        with open(help_file_path, "r") as file:
            return file.read()
    else:
        return "Help file not found."


def main() -> None:
    """
    Main function to run the program.

    It checks the operating system and the presence of an NVIDIA graphics card,
    then launches the appropriate interface or displays relevant messages.

    Usage:
        To run the GUI version: python(3) main.py --gui or python(3) main.py -g
        To run the console version: python(3) main.py --console or python(3) main.py -c
        To display this help message: python(3) main.py --help or python(3) main.py -h
        To display the settings interface: python(3) main.py --settings or python(3) main.py -s
    """

    if any(arg in sys.argv for arg in HELP_ARGS):
        print(main.__doc__)
        help_text = get_help_text()
        print(f"\n{'*' * 50}\n" "\nAdditional Help Text:" "\n")
        print(help_text)
        sys.exit(0)

    logging.debug("Starting program...")

    if platform.system() == "Windows":
        print("This program is intended for Linux and is not supported on Windows.")
        sys.exit(1)
    else:
        if not nvidia_checker.CheckNvidia().is_nvidia_gpu_present():
            print(
                "\nThe full functionality of the program can be obtained only with an Nvidia video card."
                "\nIf you have an NVIDIA graphics card, check if the drivers are installed."
                "\nTry(Ubuntu): sudo ubuntu-drivers autoinstall"
                "\n"
            )
            if not ask_user_to_continue():
                sys.exit(0)

        if json_status():
            if len(sys.argv) > 1:
                if any(arg in sys.argv for arg in GUI_ARGS):
                    gui = gui_interface.gui_interface.GuiInterface()
                    gui.run()
                elif any(arg in sys.argv for arg in CONSOLE_ARGS):
                    console = console_interface.console_interface.ConsoleInterface()
                    console.run()
                elif any(arg in sys.argv for arg in SETTINGS_ARGS):
                    settings = settings_interface.settings_window.SettingsWindow()
                    settings.run()
            else:
                greeting = greeting_interface.window.MainWindow()
                greeting.run()


if __name__ == "__main__":
    main()
