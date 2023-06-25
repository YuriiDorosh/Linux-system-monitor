class SystemInfo:
    cpu_percent_interval = 0.1  # Default 0.1 (if more - slower, less - faster)


class ScreenRecording:
    """
    A class representing screen recording functionality.

    Attributes:
        video_extension (str): The default video extension for recorded videos. By default, it is set to "mp4".
            FFmpeg supports other video formats as well, such as AVI, MKV, MOV, WMV, FLV, WebM, MPEG, 3GP, and TS.
        frame_rate (int): The frame rate at which the screen recording will be captured. By default, it is set to 30 frames per second (fps).
            You can modify this value to a smaller or larger frame rate depending on your requirements and system capabilities.
    Usage:
    To use the `ScreenRecording` class, create an instance of the class and access its attributes and methods.
    Notes:
        - You can modify the `video_extension` attribute to set a different default video extension for your recordings.
        - The supported video formats depend on the availability and configuration of FFmpeg on your system.
        - The `frame_rate` attribute determines the number of frames per second captured in the screen recording.
          Adjust this value based on your desired output and system capabilities.
    """

    video_extension: str = "mp4"  # Default mp4, but FFmpeg supports other formats too:
    # .avi - Audio Video Interleave video container format.
    # .mkv - Matroska multimedia container format.
    # .mov - QuickTime multimedia container format.
    # .wmv - Windows Media Video format.
    # .flv - Flash Video format.
    # .webm - WebM multimedia container format.
    # .mpeg - MPEG video format.
    # .3gp - 3GPP multimedia container format.
    # .ts - MPEG Transport Stream container format.

    frame_rate: int = 30  # Default 30, but you can change this value to a smaller side or, if your system allows, to a larger one
