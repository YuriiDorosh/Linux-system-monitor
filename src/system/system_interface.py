from . import system_info


class SystemInterface:
    """
    A class that provides an interface to retrieve system information and generate progress bars.

    Attributes:
        system_info (system_info.SystemInfo): An instance of the SystemInfo class for retrieving system information.

    Methods:
        get_progress_bars(): Retrieves system information and returns a list of progress bars.
        get_disk_info(): Retrieves disk information and returns it as a string.

    Usage:
        1. Initialize an instance of the SystemInterface class:
            sys_interface = SystemInterface()

        2. Access the interface methods:
            progress_bars = sys_interface.get_progress_bars()
            disk_info = sys_interface.get_disk_info()

    Notes:
        - The SystemInterface class depends on the system_info module.
    """

    def __init__(self):
        self.system_info = system_info.SystemInfo()

    def get_progress_bars(self):
        """
        Retrieves system information and returns a list of progress bars.

        Returns:
            progress_bars (list): A list of progress bars representing CPU load, memory usage, disk usage, and GPU usage.
        """
        cpu_load = self.system_info.get_cpu_load()
        memory_usage = self.system_info.get_memory_usage()
        memory_usage_gb = self.system_info.get_memory_usage_gb()
        max_memory = self.system_info.get_max_memory()
        disk_usage = self.system_info.get_disk_usage()
        gpu_usage = self.system_info.get_gpu_usage()
        cpu_frequency = self.system_info.get_cpu_frequency()
        gpu_frequency = self.system_info.get_gpu_frequency()
        max_cpu_frequency = self.system_info.get_max_cpu_frequency()
        battery_status = self.system_info.get_battery_status()

        progress_bars = [f"CPU{i + 1}: {load}%" for i, load in enumerate(cpu_load)] + [
            f"GPU: {gpu_usage}%",
            f"CPU Frequency: \n {round(cpu_frequency, 2)} MHz / {max_cpu_frequency} MHz",
            f"GPU Frequency: {gpu_frequency} MHz",
            f"RAM: {memory_usage}% ({round(memory_usage_gb, 2)} / {round(max_memory, 2)} GB)",
            f"Disk: {disk_usage}%",
        ]

        if battery_status is not None:
            battery_percent = self.system_info.get_battery_percent()
            progress_bars.append(f"Battery: {battery_percent}% - {battery_status}")

        return progress_bars

    def get_disk_info(self):
        """
        Retrieves the disk information and returns it as a string.

        Returns:
            disk_info (str): Disk free space information.
        """
        disk_info = f"Disk Free Space: {self.system_info.get_disk_free_space():.2f} GB"
        return disk_info


class ExtendedSystemInterface(SystemInterface):
    """
    A class that extends the SystemInterface class with additional methods to retrieve specific system information.

    Methods:
        get_average_cpu_load(): Calculates and returns the average CPU load.
        get_gpu_usage_percentage(): Retrieves the GPU usage and returns it as a string.
        get_memory_usage_gb(): Retrieves the memory usage and maximum memory and returns it as a string.

    Usage:
        1. Initialize an instance of the ExtendedSystemInterface class:
            extended_sys_interface = ExtendedSystemInterface()

        2. Access the extended interface methods:
            avg_cpu_load = extended_sys_interface.get_average_cpu_load()
            gpu_usage = extended_sys_interface.get_gpu_usage_percentage()
            memory_usage = extended_sys_interface.get_memory_usage_gb()

    Notes:
        - The ExtendedSystemInterface class extends the functionality of the SystemInterface class.
    """

    def __init__(self):
        super().__init__()

    def get_average_cpu_load(self):
        """
        Calculates and returns the average CPU load.

        Returns:
            average_load (str): The average CPU load.

        Example:
            avg_cpu_load = extended_sys_interface.get_average_cpu_load()
            print(avg_cpu_load)  # Output: "AVG CPU: 45.23%"
        """
        cpu_load = self.system_info.get_cpu_load()
        average_load = round(sum(cpu_load) / len(cpu_load), 2)

        return f"AVG CPU: {average_load}%"

    def get_gpu_usage_percentage(self):
        """
        Retrieves the GPU usage and returns it as a string.

        Returns:
            gpu_usage (str): GPU usage information.

        Example:
            gpu_usage = extended_sys_interface.get_gpu_usage_percentage()
            print(gpu_usage)  # Output: "GPU: 54%"
        """
        gpu_usage = self.system_info.get_gpu_usage()
        return f"GPU: {gpu_usage}%"

    def get_memory_usage_gb(self):
        """
        Retrieves the memory usage and maximum memory and returns it as a string.

        Returns:
            memory_usage (str): Memory usage information.

        Example:
            memory_usage = extended_sys_interface.get_memory_usage_gb()
            print(memory_usage)  # Output: "RAM: 4.21 GB / 16.0 GB"
        """
        memory_usage_gb = self.system_info.get_memory_usage_gb()
        max_memory = self.system_info.get_max_memory()
        return f"RAM: {round(memory_usage_gb, 2)} GB / {round(max_memory, 2)} GB"
