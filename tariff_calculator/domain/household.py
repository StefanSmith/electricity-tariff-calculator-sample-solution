class Household:
    def __init__(self, name, monthly_appliance_usage):
        self.__name = name
        self.__monthly_appliance_usage = monthly_appliance_usage

    @property
    def name(self):
        return self.__name

    @property
    def monthly_kwh(self):
        daytime_kwh = 0
        nighttime_kwh = 0

        for appliance_usage in self.__monthly_appliance_usage:
            daytime_kwh += appliance_usage.daytime_kwh
            nighttime_kwh += appliance_usage.nighttime_kwh

        return daytime_kwh, nighttime_kwh
