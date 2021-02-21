from decimal import Decimal

from domain.appliance import Appliance
from domain.appliance_usage import ApplianceUsage
from domain.household import Household
from integration.csv_file.csv_file_entity_source import CsvFileEntitySource


class CsvFileHouseholdSource(CsvFileEntitySource):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__households = []
        self.__appliance_names = []
        self.__appliances = {}

    def get_households(self):
        self.parse_file()
        return self.__households

    def _handle_electrical_appliances_header_row(self, cells):
        self.__appliance_names.extend([column_name.replace(' (W)', '') for column_name in cells])

    def _handle_electrical_appliances_data_row(self, cells):
        self.__appliances.update(**{
            self.__appliance_names[column_index]: Appliance(consumption_watts=Decimal(appliance_consumption))
            for column_index, appliance_consumption in enumerate(cells)
        })

    def _handle_households_header_row(self, cells):
        self.__appliance_names.extend([
            column_name.replace(' (day hours/night hours)', '')
            for column_name in cells[1:]
        ])

    def _handle_households_data_row(self, cells):
        self.__households.append(Household(
            name=str(cells[0]),
            monthly_appliance_usage=[
                ApplianceUsage(
                    appliance=self.__appliances[self.__appliance_names[column_index]],
                    daytime_hours=Decimal(self.__parse_daytime_hours(monthly_usage)),
                    nighttime_hours=Decimal(self.__parse_nighttime_hours(monthly_usage))
                )
                for column_index, monthly_usage in enumerate(cells[1:])
            ]
        ))

    @classmethod
    def __parse_daytime_hours(cls, monthly_consumption):
        monthly_usage_strings = cls.__get_monthly_usage_strings(monthly_consumption)
        return monthly_usage_strings[0].replace('d', '') if monthly_usage_strings[0].endswith('d') else '0'

    @classmethod
    def __parse_nighttime_hours(cls, monthly_consumption):
        monthly_usage_strings = cls.__get_monthly_usage_strings(monthly_consumption)

        if len(monthly_usage_strings) == 1:
            return monthly_usage_strings[0].replace('n', '') if monthly_usage_strings[0].endswith('n') else '0'
        else:
            return monthly_usage_strings[1].replace('n', '')

    @staticmethod
    def __get_monthly_usage_strings(monthly_consumption):
        return monthly_consumption.split('/')
