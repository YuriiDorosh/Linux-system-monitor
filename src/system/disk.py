import psutil


class Disk:
    """
    A class that provides methods to retrieve disk-related information.

    Methods:
        get_disk_usage() -> float: Returns the disk usage as a percentage.
        get_disk_free_space() -> float: Returns the available free space on the disk in gigabytes (GB).

    Usage:
        1. Initialize an instance of the Disk class:
            disk = Disk()

        2. Access the methods to retrieve disk information:
            disk_usage = disk.get_disk_usage()
            disk_free_space = disk.get_disk_free_space()

    Notes:
        - The Disk class depends on the psutil module for disk information.
    """

    @staticmethod
    def get_disk_usage() -> float:
        """
        Returns the disk usage as a percentage.

        Returns:
            float: Disk usage as a percentage.

        Example:
            disk = Disk()
            disk_usage = disk.get_disk_usage()
            print(disk_usage)  # Output: 83.7
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.percent

    @staticmethod
    def get_disk_free_space() -> float:
        """
        Returns the available free space on the disk in gigabytes (GB).

        Returns:
            float: Available free space on the disk in gigabytes (GB).

        Example:
            disk = Disk()
            disk_free_space = disk.get_disk_free_space()
            print(disk_free_space)  # Output: 214.5
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.free / (1024**3)
