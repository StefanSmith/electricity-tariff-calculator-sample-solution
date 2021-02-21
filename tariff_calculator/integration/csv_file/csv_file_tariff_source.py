from decimal import Decimal

from domain.tariff import Tariff
from integration.csv_file.csv_file_entity_source import CsvFileEntitySource


class CsvFileTariffSource(CsvFileEntitySource):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__tariffs = []

    def get_tariffs(self):
        self.parse_file()
        return self.__tariffs

    def _handle_tariffs_data_row(self, cell):
        self.__tariffs.append(Tariff(
            name=str(cell[0]),
            standing_charge_pounds=Decimal(cell[1]),
            day_unit_cost_pounds_per_kw=Decimal(cell[2]),
            night_unit_cost_pounds_per_kw=Decimal(cell[3]),
            monthly_discount_kwh_threshold=Decimal(cell[4]),
            monthly_discount_percent=Decimal(cell[5])
        ))
