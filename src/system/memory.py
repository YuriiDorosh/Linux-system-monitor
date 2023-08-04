import psutil


class Memory:
    @staticmethod
    def get_memory_usage():
        """
        Returns the memory usage as a percentage.

        Returns:
            float: Memory usage as a percentage.

        Example:
            memory = Memory()
            memory_usage = memory.get_memory_usage()
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
            memory = Memory()
            memory_usage_gb = memory.get_memory_usage_gb()
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
            memory = Memory()
            max_memory_gb = memory.get_max_memory()
            print(max_memory_gb)  # Output: 16.0
        """
        memory = psutil.virtual_memory()
        max_memory_gb = memory.total / (1024**3)
        return max_memory_gb
