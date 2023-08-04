import psutil
from typing import Optional


class Battery:
    """
    A class that provides methods to retrieve battery-related information.

    Methods:
        get_battery_status() -> Optional[str]: Retrieves battery status information.
        get_battery_percent() -> Optional[float]: Retrieves battery percentage.

    Usage:
        1. Initialize an instance of the Battery class:
            battery = Battery()

        2. Access the methods to retrieve battery information:
            battery_status = battery.get_battery_status()
            battery_percent = battery.get_battery_percent()

    Notes:
        - The Battery class depends on the psutil module for battery information.
    """

    @staticmethod
    def get_battery_status() -> Optional[str]:
        """
        Retrieves battery status information.

        Returns:
            str or None: Battery status information (e.g., "Charging", "Discharging") or None if not supported.

        Example:
            battery = Battery()
            battery_status = battery.get_battery_status()
            print(battery_status)  # Output: "Charging"
        """
        battery = psutil.sensors_battery()

        if battery:
            status = "Charging" if battery.power_plugged else "Discharging"
            return status

        return None

    @staticmethod
    def get_battery_percent() -> Optional[float]:
        """
        Retrieves battery percentage.

        Returns:
            float or None: Battery percentage or None if not supported.

        Example:
            battery = Battery()
            battery_percent = battery.get_battery_percent()
            print(battery_percent)  # Output: 90.0
        """
        battery = psutil.sensors_battery()

        if battery:
            return battery.percent

        return None
