from domain.household_result import HouseholdResult


class TariffCalculator:
    def __init__(self, tariff_source):
        self.__tariff_source = tariff_source

    def determine_cheapest_tariff_for(self, household):
        daytime_kwh, nighttime_kwh = household.monthly_kwh

        cheapest_tariff = min(
            self.__tariff_source.get_tariffs(),
            key=lambda tariff: tariff.get_monthly_cost_pounds(daytime_kwh, nighttime_kwh)
        )

        monthly_cost_pounds = cheapest_tariff.get_monthly_cost_pounds(daytime_kwh, nighttime_kwh)

        return HouseholdResult(household, cheapest_tariff, monthly_cost_pounds)
