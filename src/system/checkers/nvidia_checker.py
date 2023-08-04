import pynvml


class CheckNvidia:
    """
    A class that checks the presence of an NVIDIA graphics card on the system.

    Methods:
        is_nvidia_gpu_present() -> bool: Checks the presence of an NVIDIA graphics card on the system.

    Usage:
        1. Initialize an instance of the CheckNvidia class:
            nvidia_checker = CheckNvidia()

        2. Access the method to check for an NVIDIA GPU:
            is_present = nvidia_checker.is_nvidia_gpu_present()
            if is_present:
                print("NVIDIA GPU is present.")
            else:
                print("No NVIDIA GPU found.")

    Notes:
        - The CheckNvidia class depends on the pynvml module for NVIDIA GPU information.
    """

    def __init__(self):
        """
        Initializes the CheckNvidia class and initializes the pynvml library.
        """
        pynvml.nvmlInit()

    def __del__(self):
        """
        Shuts down the pynvml library when the instance is destroyed.
        """
        pynvml.nvmlShutdown()

    @staticmethod
    def is_nvidia_gpu_present() -> bool:
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