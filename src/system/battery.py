import psutil


class Battery:
    @staticmethod
    def get_battery_status():
        """
        Retrieves battery status information.

        Returns:
            str or None: Battery status information or None if not supported.

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
    def get_battery_percent():
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
