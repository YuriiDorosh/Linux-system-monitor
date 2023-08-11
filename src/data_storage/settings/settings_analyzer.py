import json
import os
import consts
from typing import NamedTuple


class SettingsStatus(NamedTuple):
    exists: bool
    status: str  # Could be "valid", "default", "corrupt"


def write_default_settings():
    with open(consts.SETTINGS_PATH, "w") as file:
        json.dump(consts.DEFAULT_SETTINGS, file)


def check_settings_file() -> SettingsStatus:
    if not os.path.isfile(consts.SETTINGS_PATH):
        write_default_settings()
        return SettingsStatus(exists=False, status="default")

    try:
        with open(consts.SETTINGS_PATH, "r") as file:
            settings = json.load(file)
            if settings == consts.DEFAULT_SETTINGS:
                return SettingsStatus(exists=True, status="default")
            else:
                return SettingsStatus(exists=True, status="valid")
    except json.JSONDecodeError:
        write_default_settings()
        return SettingsStatus(exists=True, status="corrupt")


# Testing the function
result = check_settings_file()
print(result.exists, result.status)
