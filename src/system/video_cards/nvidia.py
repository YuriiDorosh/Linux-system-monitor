import pynvml


class Nvidia:
    """
    A class that provides methods to retrieve NVIDIA GPU-related information.

    Methods:
        get_gpu_usage() -> int: Returns the GPU usage as a percentage if an NVIDIA GPU is available, otherwise returns 0.
        get_gpu_frequency() -> int: Returns the current frequency of the GPU in megahertz (MHz) if an NVIDIA GPU is available, otherwise returns 0.

    Usage:
        1. Initialize an instance of the Nvidia class:
            nvidia = Nvidia()

        2. Access the methods to retrieve NVIDIA GPU information:
            gpu_usage = nvidia.get_gpu_usage()
            gpu_frequency = nvidia.get_gpu_frequency()

    Notes:
        - The Nvidia class depends on the pynvml module for NVIDIA GPU information.
    """

    def __init__(self):
        self._pynvml_initialized = False

    def _initialize_pynvml(self):
        if not self._pynvml_initialized:
            pynvml.nvmlInit()
            self._pynvml_initialized = True

    def get_gpu_usage(self) -> int:
        """
        Returns the GPU usage as a percentage if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: GPU usage as a percentage or 0 if no NVIDIA GPU is available.

        Example:
            nvidia = Nvidia()
            gpu_usage = nvidia.get_gpu_usage()
            print(gpu_usage)  # Output: 54
        """
        self._initialize_pynvml()

        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            device_name = pynvml.nvmlDeviceGetName(handle)

            if "NVIDIA" in device_name:
                utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
                return utilization.gpu

        return 0

    def get_gpu_frequency(self) -> int:
        """
        Returns the current frequency of the GPU if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: Current frequency of the GPU in megahertz (MHz) or 0 if no NVIDIA GPU is available.

        Example:
            nvidia = Nvidia()
            gpu_frequency = nvidia.get_gpu_frequency()
            print(gpu_frequency)  # Output: 1750
        """
        self._initialize_pynvml()

        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            device_name = pynvml.nvmlDeviceGetName(handle)

            if "NVIDIA" in device_name:
                clock_info = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)
                return clock_info / 1000  # Convert to MHz

        return 0
