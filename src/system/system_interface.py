from . import system_info


class SystemInterface:
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

        progress_bars = [f"CPU{i + 1}: {load}%" for i, load in enumerate(cpu_load)] + [
            f"GPU: {gpu_usage}%",
            f"CPU Frequency: \n {round(cpu_frequency, 2)} MHz / {max_cpu_frequency} MHz",
            f"GPU Frequency: {gpu_frequency} MHz",
            f"RAM: {memory_usage}%({round(memory_usage_gb, 2)} / {round(max_memory, 2)}gb)",
            f"Disk: {disk_usage}%",
        ]

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
    def __init__(self):
        super().__init__()

    def get_average_cpu_load(self):
        """
        Calculates and returns the average CPU load.

        Returns:
            average_load (str): The average CPU load.
        """
        cpu_load = self.system_info.get_cpu_load()
        average_load = round(sum(cpu_load) / len(cpu_load), 2)

        return f"AVG CPU: {average_load}%"

    def get_gpu_usage_percentage(self):
        """
        Retrieves the GPU usage and returns it as a string.

        Returns:
            gpu_usage (str): GPU usage information.
        """
        gpu_usage = self.system_info.get_gpu_usage()
        return f"GPU: {gpu_usage}%"

    def get_memory_usage_gb(self):
        """
        Retrieves the memory usage and maximum memory and returns it as a string.

        Returns:
            memory_usage (str): Memory usage information.
        """
        memory_usage_gb = self.system_info.get_memory_usage_gb()
        max_memory = self.system_info.get_max_memory()
        return f"RAM:{round(memory_usage_gb, 2)} / {round(max_memory, 2)}gb"
