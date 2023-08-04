import psutil
import pynvml

import settings


class SystemInfo:
    """
    A class that provides system information such as CPU load, memory usage, disk usage, GPU usage, and disk free space.

    Attributes:
        _pynvml_initialized (bool): Flag indicating whether the pynvml module has been initialized.

    Methods:
        get_cpu_load(): Returns the CPU load as a percentage for each CPU core.
        get_memory_usage(): Returns the memory usage as a percentage.
        get_memory_usage_gb(): Returns the memory usage in gigabytes (GB).
        get_max_memory(): Returns the maximum available memory in gigabytes (GB).
        get_disk_usage(): Returns the disk usage as a percentage.
        get_gpu_usage(): Returns the GPU usage as a percentage if an NVIDIA GPU is available, otherwise returns 0.
        get_disk_free_space(): Returns the available free space on the disk in gigabytes (GB).
        get_cpu_frequency(): Returns the current frequency of the CPU in megahertz (MHz).
        get_gpu_frequency(): Returns the current frequency of the GPU in megahertz (MHz) if an NVIDIA GPU is available, otherwise returns 0.
        get_max_cpu_frequency(): Returns the maximum CPU frequency in megahertz (MHz).
        get_battery_status(): Retrieves battery status information (if available).
        get_battery_percent(): Retrieves battery percentage (if available).





    Usage:
        1. Initialize an instance of the SystemInfo class:
            system_info = SystemInfo()

        2. Access the system information methods:
            cpu_load = system_info.get_cpu_load()
            memory_usage = system_info.get_memory_usage()
            memory_usage_gb = system_info.get_memory_usage_gb()
            max_memory_gb = system_info.get_max_memory()
            disk_usage = system_info.get_disk_usage()
            gpu_usage = system_info.get_gpu_usage()
            disk_free_space = system_info.get_disk_free_space()
            cpu_frequency = system_info.get_cpu_frequency()
            gpu_frequency = system_info.get_gpu_frequency()
            max_cpu_frequency = system_info.get_max_cpu_frequency()
            battery_status = system_info.get_battery_status()
            battery_percent = system_info.get_battery_percent()

    Notes:
        - The SystemInfo class depends on the psutil and pynvml modules.
        - The pynvml module is used for GPU information and requires an NVIDIA GPU and the appropriate drivers to be installed.
        - The CPU load is provided as a percentage for each CPU core.
        - Memory usage and disk usage are reported as percentages.
        - Memory usage is also reported in gigabytes (GB).
        - Disk free space is reported in gigabytes (GB).
        - CPU and GPU frequencies are reported in megahertz (MHz).
        - Battery status and percentage are reported if supported by the system. Otherwise, None is returned.
    """

    def __init__(self):
        self._pynvml_initialized = False

    @staticmethod
    def get_cpu_load():
        """
        Returns the CPU load as a percentage for each CPU core.

        Returns:
            list: A list of CPU load percentages for each CPU core.

        Example:
            cpu_load = SystemInfo.get_cpu_load()
            print(cpu_load)  # Output: [30.2, 40.5, 20.1, ...]
        """
        return psutil.cpu_percent(
            interval=settings.SystemInfo.cpu_percent_interval, percpu=True
        )

    @staticmethod
    def get_memory_usage():
        """
        Returns the memory usage as a percentage.

        Returns:
            float: Memory usage as a percentage.

        Example:
            memory_usage = SystemInfo.get_memory_usage()
            print(memory_usage)  # Output: 65.3
        """
        return psutil.virtual_memory().percent

    @staticmethod
    def get_memory_usage_gb():
        """
        Returns the memory usage in gigabytes (GB).

        Returns:
            float: Memory usage in gigabytes (GB).

        Example:
            memory_usage_gb = SystemInfo.get_memory_usage_gb()
            print(memory_usage_gb)  # Output: 4.2
        """
        memory = psutil.virtual_memory()
        memory_gb = memory.used / (1024**3)
        return memory_gb

    @staticmethod
    def get_max_memory():
        """
        Returns the maximum available memory in gigabytes (GB).

        Returns:
            float: Maximum available memory in gigabytes (GB).

        Example:
            max_memory_gb = SystemInfo.get_max_memory()
            print(max_memory_gb)  # Output: 16.0
        """
        memory = psutil.virtual_memory()
        max_memory_gb = memory.total / (1024**3)
        return max_memory_gb

    @staticmethod
    def get_disk_usage():
        """
        Returns the disk usage as a percentage.

        Returns:
            float: Disk usage as a percentage.

        Example:
            disk_usage = SystemInfo.get_disk_usage()
            print(disk_usage)  # Output: 83.7
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.percent

    @staticmethod
    def get_battery_status():
        """
        Retrieves battery status information.

        Returns:
            battery_info (str or None): Battery status information or None if not supported.

        Example:

            battery_status = sys_interface.get_battery_status()

            battery_status = SystemInfo.get_battery_status()

            print(battery_status)  # Output: "Battery: 90% - Charging"
        """
        battery = psutil.sensors_battery()

        if battery:
            status = "Charging" if battery.power_plugged else "Discharging"
            return status

        return None

    @staticmethod
    def get_battery_percent():
        """
        Retrieves battery percentage.

        Returns:
            battery_percent (float or None): Battery percentage or None if not supported.

        Example:

            battery_percent = sys_interface.get_battery_percent()

            battery_percent = SystemInfo.get_battery_percent()

            print(battery_percent)  # Output: 90.0
        """
        battery = psutil.sensors_battery()

        if battery:
            return battery.percent

        return None

    def get_gpu_usage(self):
        """
        Returns the GPU usage as a percentage if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: GPU usage as a percentage or 0 if no NVIDIA GPU is available.

        Example:
            gpu_usage = SystemInfo.get_gpu_usage()
            print(gpu_usage)  # Output: 54
        """
        if not self._pynvml_initialized:
            pynvml.nvmlInit()
            self._pynvml_initialized = True

        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            device_name = pynvml.nvmlDeviceGetName(handle)

            if "NVIDIA" in device_name:
                utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
                return utilization.gpu

        return 0

    @staticmethod
    def get_cpu_frequency():
        """
        Returns the current frequency of the CPU in megahertz (MHz).

        Returns:
            int: Current frequency of the CPU in megahertz (MHz).

        Example:
            cpu_frequency = SystemInfo.get_cpu_frequency()
            print(cpu_frequency)  # Output: 2400
        """
        return psutil.cpu_freq().current

    def get_gpu_frequency(self):
        """
        Returns the current frequency of the GPU if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: Current frequency of the GPU in megahertz (MHz) or 0 if no NVIDIA GPU is available.

        Example:
            gpu_frequency = SystemInfo.get_gpu_frequency()
            print(gpu_frequency)  # Output: 1750
        """
        if not self._pynvml_initialized:
            pynvml.nvmlInit()
            self._pynvml_initialized = True

        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            device_name = pynvml.nvmlDeviceGetName(handle)

            if "NVIDIA" in device_name:
                clock_info = pynvml.nvmlDeviceGetClockInfo(
                    handle, pynvml.NVML_CLOCK_GRAPHICS
                )
                return clock_info / 1000  # Convert to MHz

        return 0

    @staticmethod
    def get_max_cpu_frequency():
        """
        Returns the maximum CPU frequency in megahertz (MHz).

        Returns:
            int: Maximum CPU frequency in megahertz (MHz).

        Example:
            max_cpu_frequency = SystemInfo.get_max_cpu_frequency()
            print(max_cpu_frequency)  # Output: 4000
        """
        return psutil.cpu_freq().max

    @staticmethod
    def get_disk_free_space():
        """
        Returns the available free space on the disk in gigabytes (GB).

        Returns:
            float: Available free space on the disk in gigabytes (GB).

        Example:
            disk_free_space = SystemInfo.get_disk_free_space()
            print(disk_free_space)  # Output: 214.5
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.free / (1024**3)
