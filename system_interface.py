from system_info import SystemInfo


class SystemInterface:
    def __init__(self):
        self.system_info = SystemInfo()

    def get_progress_bars(self):
        cpu_load = self.system_info.get_cpu_load()
        memory_usage = self.system_info.get_memory_usage()
        disk_usage = self.system_info.get_disk_usage()
        gpu_usage = self.system_info.get_gpu_usage()

        progress_bars = [f"CPU{i + 1}: {load}%" for i, load in enumerate(cpu_load)] + [
            f"Memory: {memory_usage}%",
            f"Disk: {disk_usage}%",
            f"GPU: {gpu_usage}%",
        ]

        return progress_bars

    def get_disk_info(self):
        disk_info = f"Disk Free Space: {self.system_info.get_disk_free_space():.2f} GB"
        return disk_info


class ExtendedSystemInterface(SystemInterface):
    def __init__(self):
        super().__init__()

    def get_average_cpu_load(self):
        cpu_load = self.system_info.get_cpu_load()
        average_load = round(sum(cpu_load) / len(cpu_load), 2)

        return f"AVG CPU: {average_load}%"

    def get_gpu_usage_percentage(self):
        gpu_usage = self.system_info.get_gpu_usage()
        return f"GPU: {gpu_usage}%"
