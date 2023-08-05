import json


class SystemInfo:
    """
    A class for handling system information settings_interface.

    Attributes:
        cpu_percent_interval (float): Interval for measuring CPU load in seconds. Default value is 0.1.
    """

    cpu_percent_interval: float = 0.1


class ScreenRecording:
    """
    A class for handling screen recording settings_interface.

    Attributes:
        video_extension (str): Video extension for recording. Default value is "mp4".
        frame_rate (int): Frame rate for recording. Default value is 30.
        monitor_resolution (str): Monitor resolution for recording. Default value is "1920x1080".
    """

    video_extension: str = "mp4"
    frame_rate: int = 30
    monitor_resolution: str = "1920x1080"


class KeyBindings:
    """
    A class for handling key bindings settings_interface.

    Attributes:
        topmost (str): Key binding for "topmost" action. Default value is "<Control-t>".
        start_recording (str): Key binding for "start recording" action. Default value is "<Control-r>".
        minimalize (str): Key binding for "minimalize" action. Default value is "<Control-m>".
        screenshot (str): Key binding for "screenshot" action. Default value is "<Control-s>".
    """

    topmost = "<Control-t>"
    start_recording = "<Control-r>"
    minimalize = "<Control-m>"
    screenshot = "<Control-s>"


def load_settings_from_json(file_path: str) -> None:
    """
    Load settings_interface from a specified JSON file.

    This function will attempt to load settings_interface from the given JSON file and will set default values if the file or specific fields are not found.

    Args:
        file_path (str): Path to the JSON file containing settings_interface.

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        ValueError: If there is an error decoding the JSON in the file.
    """
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            SystemInfo.cpu_percent_interval = data.get("cpu_percent_interval", 0.1)
            ScreenRecording.video_extension = data.get("video_format", "mp4")
            ScreenRecording.frame_rate = data.get("fps", 30)
            ScreenRecording.monitor_resolution = data.get(
                "monitor_resolution", "1920x1080"
            )
            KeyBindings.topmost = data.get("topmost", "<Control-t>")
            KeyBindings.start_recording = data.get("start_recording", "<Control-r>")
            KeyBindings.minimalize = data.get("minimalize", "<Control-m>")
            KeyBindings.screenshot = data.get("screenshot", "<Control-s>")
    except FileNotFoundError:
        print(f"Settings file not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in settings_interface file: {file_path}")


settings_file_path = "data_storage/settings/settings.json"
load_settings_from_json(settings_file_path)
