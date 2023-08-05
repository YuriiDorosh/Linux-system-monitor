import json
import os


def check_settings_file():
    settings_path = "data_storage/settings/settings.json"
    default_settings = {"cpu_percent_interval": 0.1, "video_format": "mp4", "fps": 30,
                        "monitor_resolution": "1920x1080", "topmost": "<Control-t>", "start_recording": "<Control-r>",
                        "minimalize": "<Control-m>", "screenshot": "<Control-s>"}

    if not os.path.isfile(settings_path):
        with open(settings_path, 'w') as file:
            json.dump(default_settings, file)
        return False

    try:
        with open(settings_path, 'r') as file:
            settings = json.load(file)
            if settings == default_settings:
                return True
    except json.JSONDecodeError:
        with open(settings_path, 'w') as file:
            json.dump(default_settings, file)
        return False

    return False
