import psutil
import importlib


module_name = "settings"
settings = importlib.import_module(module_name)


class Processor:
    """
    A class that provides methods to retrieve CPU-related information.

    Attributes:
        system_info (settings_interface.SystemInfo): An instance of the SystemInfo class for
        retrieving system information.

    Methods:
        get_cpu_load() -> List[float]: Returns the CPU load as a percentage for each CPU core.
        get_cpu_frequency() -> int: Returns the current frequency of the CPU in megahertz (MHz).
        get_max_cpu_frequency() -> int: Returns the maximum CPU frequency in megahertz (MHz).
        check_info() -> None: Prints information about the CPU, including load and frequency.

    Usage:
        1. Initialize an instance of the Processor class:
            processor = Processor()

        2. Access the methods to retrieve CPU information:
            cpu_load = processor.get_cpu_load()
            cpu_frequency = processor.get_cpu_frequency()
            max_cpu_frequency = processor.get_max_cpu_frequency()
            processor.check_info()

    Notes:
        - The Processor class depends on the settings_interface module for system information.
    """

    def __init__(self) -> None:
        self.system_info = settings.SystemInfo()

    def get_cpu_load(self) -> float:
        """
        Returns the CPU load as a percentage for each CPU core.

        Returns:
            float: A list of CPU load percentages for each CPU core.
        """
        return float(psutil.cpu_percent(interval=self.system_info.cpu_percent_interval, percpu=True))

    def check_info(self) -> None:
        """
        Prints information about the CPU, including load and frequency.
        """
        print("CPU Information:")
        print(f"CPU Load: {self.get_cpu_load()}%")
        print(f"CPU Frequency: {self.get_cpu_frequency()} MHz")
        print(f"Max CPU Frequency: {self.get_max_cpu_frequency()} MHz")

    @staticmethod
    def get_cpu_frequency() -> float:
        """
        Returns the current frequency of the CPU in megahertz (MHz).

        Returns:
            float: Current frequency of the CPU in megahertz (MHz).
        """
        return float(psutil.cpu_freq().current)

    @staticmethod
    def get_max_cpu_frequency() -> float:
        """
        Returns the maximum CPU frequency in megahertz (MHz).

        Returns:
            float: Maximum CPU frequency in megahertz (MHz).
        """
        return float(psutil.cpu_freq().max)
