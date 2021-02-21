from decimal import Decimal

DECIMAL_0 = Decimal('0')
DECIMAL_1 = Decimal('1')
DECIMAL_100 = Decimal('100')


class Tariff:
    def __init__(self, name, standing_charge_pounds, day_unit_cost_pounds_per_kw, night_unit_cost_pounds_per_kw,
                 monthly_discount_kwh_threshold, monthly_discount_percent):
        self.__name = name
        self.__day_unit_cost_pounds_per_kw = day_unit_cost_pounds_per_kw
        self.__night_unit_cost_pounds_per_kw = night_unit_cost_pounds_per_kw
        self.__standing_charge_pounds = standing_charge_pounds
        self.__monthly_discount_kwh_threshold = monthly_discount_kwh_threshold
        self.__monthly_discount_percent = monthly_discount_percent

    @property
    def name(self):
        return self.__name

    def get_monthly_cost_pounds(self, daytime_consumption_kwh, nighttime_consumption_kwh):
        consumption_cost = (self.__cost_of_daytime_consumption(daytime_consumption_kwh) +
                            self.__cost_of_nighttime_consumption(nighttime_consumption_kwh))

        total_consumption_kwh = daytime_consumption_kwh + nighttime_consumption_kwh

        if total_consumption_kwh == Decimal('0'):
            return self.__standing_charge_pounds

        return (self.__standing_charge_pounds +
                self.__apply_consumption_threshold_discount(consumption_cost, total_consumption_kwh))

    def __apply_consumption_threshold_discount(self, gross_cost, total_consumption_kwh):
        discounted_consumption = max(DECIMAL_0, total_consumption_kwh - self.__monthly_discount_kwh_threshold)
        discounted_cost_fraction = discounted_consumption / total_consumption_kwh
        undiscounted_cost_fraction = DECIMAL_1 - discounted_cost_fraction
        discount_residual_fraction = DECIMAL_1 - self.__monthly_discount_percent / DECIMAL_100

        return gross_cost * (undiscounted_cost_fraction + discounted_cost_fraction * discount_residual_fraction)

    def __cost_of_daytime_consumption(self, daytime_consumption_kwh):
        return daytime_consumption_kwh * self.__day_unit_cost_pounds_per_kw

    def __cost_of_nighttime_consumption(self, nighttime_consumption_kwh):
        return nighttime_consumption_kwh * self.__night_unit_cost_pounds_per_kw

    def __repr__(self):
        return self.name
