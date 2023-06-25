import psutil
import pynvml


class SystemInfo:
    def __init__(self):
        self.pynvml_initialized = False

    @staticmethod
    def get_cpu_load():
        return psutil.cpu_percent(interval=0.1, percpu=True)

    @staticmethod
    def get_memory_usage():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_disk_usage():
        disk_usage = psutil.disk_usage("/")
        return disk_usage.percent

    def get_gpu_usage(self):
        if not self.pynvml_initialized:
            pynvml.nvmlInit()
            self.pynvml_initialized = True

        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            device_name = pynvml.nvmlDeviceGetName(handle)

            if "NVIDIA" in device_name:
                utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
                return utilization.gpu

        return 0

    @staticmethod
    def get_disk_free_space():
        disk_usage = psutil.disk_usage("/")
        return disk_usage.free / (1024**3)
