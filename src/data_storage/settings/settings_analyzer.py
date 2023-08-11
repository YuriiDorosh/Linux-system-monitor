import json
import os
from typing import NamedTuple


class SettingsStatus(NamedTuple):
    exists: bool
    status: str  # Could be "valid", "default", "corrupt"


SETTINGS_PATH = "data_storage/settings/settings.json"
DEFAULT_SETTINGS = {
    "cpu_percent_interval": 0.1,
    "video_format": "mp4",
    "fps": 30,
    "monitor_resolution": "1920x1080",
    "topmost": "<Control-t>",
    "start_recording": "<Control-r>",
    "minimalize": "<Control-m>",
    "screenshot": "<Control-s>",
}


def write_default_settings():
    with open(SETTINGS_PATH, "w") as file:
        json.dump(DEFAULT_SETTINGS, file)


def check_settings_file() -> SettingsStatus:
    if not os.path.isfile(SETTINGS_PATH):
        write_default_settings()
        return SettingsStatus(exists=False, status="default")

    try:
        with open(SETTINGS_PATH, "r") as file:
            settings = json.load(file)
            if settings == DEFAULT_SETTINGS:
                return SettingsStatus(exists=True, status="default")
            else:
                return SettingsStatus(exists=True, status="valid")
    except json.JSONDecodeError:
        write_default_settings()
        return SettingsStatus(exists=True, status="corrupt")


# Testing the function
result = check_settings_file()
print(result.exists, result.status)
