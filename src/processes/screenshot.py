import pyautogui
import time
import os


class Screenshot:
    """
    A class that provides methods to take screenshots.

    Attributes:
        save_dir (str): The directory where the screenshots are saved.

    Methods:
        take() -> str: Captures the screenshot and returns the screenshot's file path.
    """

    def __init__(self):
        """
        Initializes the Screenshot class by setting up the directory to save the screenshots.
        """
        # Determine the path for the 'screenshots' directory relative to the current file's location
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        self.save_dir = os.path.join(base_dir, "screenshots")

        # Create the directory if it doesn't exist
        try:
            os.makedirs(self.save_dir, exist_ok=True)
        except Exception as e:
            print(f"Failed to create directory {self.save_dir}. Error: {e}")

    def take(self) -> str:
        """
        Captures the screenshot and saves it to the directory.

        Returns:
            str: The file path of the saved screenshot.
        """
        # Define the name of the screenshot
        screenshot_name = f"screenshot_{int(time.time())}.png"

        # Define the path where the screenshot will be saved
        screenshot_path = os.path.join(self.save_dir, screenshot_name)

        try:
            # Capture the screenshot
            screenshot = pyautogui.screenshot()

            # Save the screenshot
            screenshot.save(screenshot_path)

            return screenshot_path

        except Exception as e:
            print(f"Failed to capture and save screenshot. Error: {e}")
            return None

