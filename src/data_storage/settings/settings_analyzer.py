import json
import os


def check_settings_file():
    """
    Checks if a settings file exists, validates its contents and creates a new settings file with
    default values if necessary.

    This function first checks if a settings file exists at the specified location. If the file
    doesn't exist, a new file with default settings is created.

    Then, it attempts to open and load the settings file. If the contents of the file match the
    default settings, the function returns True.

    If the file contains invalid JSON data, a JSONDecodeError is thrown. The except clause catches
    this exception, writes the default settings to the file, and returns False.

    Finally, if the file exists and contains valid JSON that doesn't match the default settings,
    the function returns False.

    Returns:
        bool: True if a settings file exists and contains the default settings, False otherwise.
    """

    settings_path = "data_storage/settings/settings.json"
    default_settings = {
        "cpu_percent_interval": 0.1,
        "video_format": "mp4",
        "fps": 30,
        "monitor_resolution": "1920x1080",
        "topmost": "<Control-t>",
        "start_recording": "<Control-r>",
        "minimalize": "<Control-m>",
        "screenshot": "<Control-s>",
    }

    if not os.path.isfile(settings_path):
        with open(settings_path, "w") as file:
            json.dump(default_settings, file)
        return False

    try:
        with open(settings_path, "r") as file:
            settings = json.load(file)
            if settings == default_settings:
                return True
    except json.JSONDecodeError:
        with open(settings_path, "w") as file:
            json.dump(default_settings, file)
        return False

    return False
