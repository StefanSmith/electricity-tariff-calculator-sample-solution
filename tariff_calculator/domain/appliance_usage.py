class ApplianceUsage:
    def __init__(self, appliance, daytime_hours, nighttime_hours):
        self.__appliance = appliance
        self.__daytime_hours = daytime_hours
        self.__nighttime_hours = nighttime_hours

    @property
    def daytime_kwh(self):
        return self.__appliance.get_kwh_consumed(self.__daytime_hours)

    @property
    def nighttime_kwh(self):
        return self.__appliance.get_kwh_consumed(self.__nighttime_hours)
