import pynvml


class Nvidia:
    def __init__(self):
        self._pynvml_initialized = False

    def _initialize_pynvml(self):
        if not self._pynvml_initialized:
            pynvml.nvmlInit()
            self._pynvml_initialized = True

    def get_gpu_usage(self):
        """
        Returns the GPU usage as a percentage if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: GPU usage as a percentage or 0 if no NVIDIA GPU is available.

        Example:
            gpu = GPU()
            gpu_usage = gpu.get_gpu_usage()
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

    def get_gpu_frequency(self):
        """
        Returns the current frequency of the GPU if an NVIDIA GPU is available, otherwise returns 0.

        Returns:
            int: Current frequency of the GPU in megahertz (MHz) or 0 if no NVIDIA GPU is available.

        Example:
            gpu = GPU()
            gpu_frequency = gpu.get_gpu_frequency()
            print(gpu_frequency)  # Output: 1750
        """
        self._initialize_pynvml()

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
