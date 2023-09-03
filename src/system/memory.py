import psutil


class Memory:
    """
    A class that provides methods to retrieve memory-related information.

    Methods:
        get_memory_usage() -> float: Returns the memory usage as a percentage.
        get_memory_usage_gb() -> float: Returns the memory usage in gigabytes (GB).
        get_max_memory() -> float: Returns the maximum available memory in gigabytes (GB).

    Usage:
        1. Initialize an instance of the Memory class:
            memory = Memory()

        2. Access the methods to retrieve memory information:
            memory_usage = memory.get_memory_usage()
            memory_usage_gb = memory.get_memory_usage_gb()
            max_memory_gb = memory.get_max_memory()

    Notes:
        - The Memory class depends on the psutil module for memory information.
    """

    @staticmethod
    def get_memory_usage() -> float:
        """
        Returns the memory usage as a percentage.

        Returns:
            float: Memory usage as a percentage.

        Example:
            memory = Memory()
            memory_usage = memory.get_memory_usage()
            print(memory_usage)  # Output: 65.3
        """
        return float(psutil.virtual_memory().percent)

    @staticmethod
    def get_memory_usage_gb() -> float:
        """
        Returns the memory usage in gigabytes (GB).

        Returns:
            float: Memory usage in gigabytes (GB).

        Example:
            memory = Memory()
            memory_usage_gb = memory.get_memory_usage_gb()
            print(memory_usage_gb)  # Output: 4.2
        """
        memory = psutil.virtual_memory()
        memory_gb = memory.used / (1024**3)
        return float(memory_gb)

    @staticmethod
    def get_max_memory() -> float:
        """
        Returns the maximum available memory in gigabytes (GB).

        Returns:
            float: Maximum available memory in gigabytes (GB).

        Example:
            memory = Memory()
            max_memory_gb = memory.get_max_memory()
            print(max_memory_gb)  # Output: 16.0
        """
        memory = psutil.virtual_memory()
        max_memory_gb = memory.total / (1024**3)
        return float(max_memory_gb)
