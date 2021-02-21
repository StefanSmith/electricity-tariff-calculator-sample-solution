import sys

from domain.cheapest_tariff_report_service import CheapestTariffReportService
from integration.console.console_display import ConsoleDisplay
from integration.csv_file.csv_file_household_source import CsvFileHouseholdSource
from integration.csv_file.csv_file_tariff_source import CsvFileTariffSource


def main(input_file_path):
    tariff_source = CsvFileTariffSource(input_file_path)
    household_source = CsvFileHouseholdSource(input_file_path)
    display = ConsoleDisplay()
    report_service = CheapestTariffReportService(tariff_source, display)

    report_service.generate_report_for_households_in(household_source)


if __name__ == '__main__':
    main(sys.argv[1])
