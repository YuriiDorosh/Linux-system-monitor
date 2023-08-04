from .checkers import nvidia_checker

from .processor import Processor
from .battery import Battery
from .memory import Memory
from .disk import Disk
from .video_cards.nvidia import Nvidia

from typing import List


class SystemInterface:
    """
    A class that provides an interface to retrieve system information and generate progress bars.

    Methods:
        get_progress_bars() -> List[str]: Retrieves system information and returns a list of progress bars.

    Usage:
        1. Initialize an instance of the SystemInterface class:
            sys_interface = SystemInterface()

        2. Access the interface methods:
            progress_bars = sys_interface.get_progress_bars()

    Notes:
        - The SystemInterface class provides an interface to gather system information,
          but the implementation details for system_info methods are not included here.

    Attributes:
        processor (Processor): An instance of the Processor class to retrieve CPU-related information.
        battery (Battery): An instance of the Battery class to retrieve battery-related information.
        memory (Memory): An instance of the Memory class to retrieve memory-related information.
        disk (Disk): An instance of the Disk class to retrieve disk-related information.
        nvidia (Nvidia): An instance of the Nvidia class to retrieve NVIDIA GPU-related information.
        nvidia_checker (CheckNvidia): An instance of the CheckNvidia class to check NVIDIA GPU presence.
    """

    def __init__(self):
        self.processor = Processor()
        self.battery = Battery()
        self.memory = Memory()
        self.disk = Disk()
        self.nvidia = Nvidia()
        self.nvidia_checker = nvidia_checker.CheckNvidia()

    def get_progress_bars(self) -> List[str]:
        """
        Retrieves system information and returns a list of progress bars.

        Returns:
            progress_bars (list): A list of progress bars representing CPU load, memory usage, disk usage, and GPU usage.
        """
        cpu_load = self.processor.get_cpu_load()
        memory_usage = self.memory.get_memory_usage()
        memory_usage_gb = self.memory.get_memory_usage_gb()
        max_memory = self.memory.get_max_memory()
        disk_usage = self.disk.get_disk_usage()
        disk_free_space = self.disk.get_disk_free_space()
        cpu_frequency = self.processor.get_cpu_frequency()
        max_cpu_frequency = self.processor.get_max_cpu_frequency()
        battery_status = self.battery.get_battery_status()

        gpu_bars = []

        if self.nvidia_checker.is_nvidia_gpu_present():
            nvidia_usage = self.nvidia.get_gpu_usage()
            nvidia_frequency = self.nvidia.get_gpu_frequency()
            gpu_bars.append(f"GPU: {nvidia_usage}%")
            gpu_bars.append(
                f"GPU Frequency: {nvidia_frequency} MHz",
            )

        progress_bars = (
            [f"CPU{i + 1}: {load}%" for i, load in enumerate(cpu_load)]
            + gpu_bars
            + [
                f"CPU Frequency: \n {round(cpu_frequency, 2)} MHz / {max_cpu_frequency} MHz",
                f"RAM: {memory_usage}% ({round(memory_usage_gb, 2)} / {round(max_memory, 2)} GB)",
                f"Disk: {disk_usage}%",
                f"Disk Free Space: {disk_free_space:.2f} GB",
            ]
        )

        if battery_status is not None:
            battery_percent = self.battery.get_battery_percent()
            progress_bars.append(f"Battery: {battery_percent}% - {battery_status}")

        return progress_bars


class ExtendedSystemInterface(SystemInterface):
    """
    A class that extends the SystemInterface class with additional methods to retrieve specific system information.

    Methods:
        get_average_cpu_load() -> str: Calculates and returns the average CPU load.
        get_gpu_usage_percentage() -> str: Retrieves the GPU usage and returns it as a string.
        get_memory_usage_gb() -> str: Retrieves the memory usage and maximum memory and returns it as a string.

    Usage:
        1. Initialize an instance of the ExtendedSystemInterface class:
            extended_sys_interface = ExtendedSystemInterface()

        2. Access the extended interface methods:
            avg_cpu_load = extended_sys_interface.get_average_cpu_load()
            gpu_usage = extended_sys_interface.get_gpu_usage_percentage()
            memory_usage = extended_sys_interface.get_memory_usage_gb()

    Notes:
        - The ExtendedSystemInterface class extends the functionality of the SystemInterface class.
        - It provides additional methods for specific system information.
        - The implementation details for the extended methods are not included here and should be provided in subclasses.

    Attributes:
        Inherits all attributes from the SystemInterface class.
    """

    def __init__(self):
        super().__init__()

    def get_average_cpu_load(self) -> str:
        """
        Calculates and returns the average CPU load.

        Returns:
            average_load (str): The average CPU load.

        Example:
            avg_cpu_load = extended_sys_interface.get_average_cpu_load()
            print(avg_cpu_load)  # Output: "AVG CPU: 45.23%"
        """
        cpu_load = self.processor.get_cpu_load()
        average_load = round(sum(cpu_load) / len(cpu_load), 2)

        return f"AVG CPU: {average_load}%"

    def get_gpu_usage_percentage(self) -> str:
        """
        Retrieves the GPU usage and returns it as a string.

        Returns:
            gpu_usage (str): GPU usage information.

        Example:
            gpu_usage = extended_sys_interface.get_gpu_usage_percentage()
            print(gpu_usage)  # Output: "GPU: 54%"
        """
        if self.nvidia_checker.is_nvidia_gpu_present():
            nvidia_usage = self.nvidia.get_gpu_usage()
            return f"GPU: {nvidia_usage}%"
        else:
            return "GPU: no info"

    def get_memory_usage_gb(self) -> str:
        """
        Retrieves the memory usage and maximum memory and returns it as a string.

        Returns:
            memory_usage (str): Memory usage information.

        Example:
            memory_usage = extended_sys_interface.get_memory_usage_gb()
            print(memory_usage)  # Output: "RAM: 4.21 GB / 16.0 GB"
        """
        memory_usage_gb = self.memory.get_memory_usage_gb()
        max_memory = self.memory.get_max_memory()
        return f"RAM: {round(memory_usage_gb, 2)} GB / {round(max_memory, 2)} GB"
