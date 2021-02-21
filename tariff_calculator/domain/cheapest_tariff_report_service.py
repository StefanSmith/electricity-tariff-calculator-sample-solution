from domain.tariff_calculator import TariffCalculator


class CheapestTariffReportService:
    def __init__(self, tariff_source, display):
        self.__tariff_calculator = TariffCalculator(tariff_source=tariff_source)
        self.__display = display

    def generate_report_for_households_in(self, household_source):
        results = [
            self.__tariff_calculator.determine_cheapest_tariff_for(household)
            for household in household_source.get_households()
        ]
        self.__display.render_results(results)
