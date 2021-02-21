from decimal import Decimal


class Appliance:
    def __init__(self, consumption_watts):
        self.__consumption_watts = consumption_watts

    def get_kwh_consumed(self, hours):
        return hours * self.__consumption_watts / Decimal('1000')
