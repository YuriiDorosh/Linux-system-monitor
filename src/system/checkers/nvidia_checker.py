import pynvml


class CheckNvidia:
    def __init__(self):
        """
        Initializes the CheckNvidia class.
        """
        pynvml.nvmlInit()

    def __del__(self):
        """
        Shuts down the pynvml library when the instance is destroyed.
        """
        pynvml.nvmlShutdown()

    @staticmethod
    def is_nvidia_gpu_present():
        """
        Checks the presence of an NVIDIA graphics card on the system.

        Returns:
            bool: True if an NVIDIA graphics card is present, otherwise False.
        """
        try:
            device_count = pynvml.nvmlDeviceGetCount()
            return device_count > 0
        except pynvml.NVMLError as err:
            print(f"NVIDIA video card verification error: {err}\n")
            return False
