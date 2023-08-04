import psutil


class Disk:
    def __init__(self):
        pass

    @staticmethod
    def get_disk_usage():
        """
        Returns the disk usage as a percentage.

        Returns:
            float: Disk usage as a percentage.

        Example:
            disk_usage = Disk.get_disk_usage()
            print(disk_usage)  # Output: 83.7
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.percent

    @staticmethod
    def get_disk_free_space():
        """
        Returns the available free space on the disk in gigabytes (GB).

        Returns:
            float: Available free space on the disk in gigabytes (GB).

        Example:
            disk_free_space = Disk.get_disk_free_space()
            print(disk_free_space)  # Output: 214.5
        """
        disk_usage = psutil.disk_usage("/")
        return disk_usage.free / (1024**3)
