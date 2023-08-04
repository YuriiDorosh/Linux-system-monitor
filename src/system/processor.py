import psutil
import importlib

module_name = "settings"
settings = importlib.import_module(module_name)


class Processor:
    def __init__(self):
        self.system_info = settings.SystemInfo()

    def get_cpu_load(self):
        """
        Returns the CPU load as a percentage for each CPU core.

        Returns:
            list: A list of CPU load percentages for each CPU core.
        """

        return psutil.cpu_percent(
            interval=self.system_info.cpu_percent_interval, percpu=True
        )

    def check_info(self):
        """
        Prints information about the CPU, including load and frequency.
        """
        print("CPU Information:")
        print(f"CPU Load: {self.get_cpu_load()}%")
        print(f"CPU Frequency: {self.get_cpu_frequency()} MHz")
        print(f"Max CPU Frequency: {self.get_max_cpu_frequency()} MHz")

    @staticmethod
    def get_cpu_frequency():
        """
        Returns the current frequency of the CPU in megahertz (MHz).

        Returns:
            int: Current frequency of the CPU in megahertz (MHz).
        """
        return psutil.cpu_freq().current

    @staticmethod
    def get_max_cpu_frequency():
        """
        Returns the maximum CPU frequency in megahertz (MHz).

        Returns:
            int: Maximum CPU frequency in megahertz (MHz).
        """
        return psutil.cpu_freq().max
