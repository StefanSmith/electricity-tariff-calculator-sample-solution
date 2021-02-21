import csv
from abc import ABCMeta

ELECTRICAL_APPLIANCES_SECTION_HEADER = 'Electrical Appliances'
ELECTRICAL_APPLIANCES_SECTION_FIRST_COLUMN_NAME = 'Washing machine (W)'

TARIFFS_SECTION_HEADER = 'Tariffs'
TARIFFS_SECTION_FIRST_COLUMN_NAME = 'Tariff'

HOUSEHOLDS_SECTION_HEADER = 'Household Monthly Usage (Day & Night Hours)'
HOUSEHOLDS_SECTION_FIRST_COLUMN_NAME = 'Household'

SECTION_HEADERS = [
    ELECTRICAL_APPLIANCES_SECTION_HEADER,
    TARIFFS_SECTION_HEADER,
    HOUSEHOLDS_SECTION_HEADER
]


class CsvFileEntitySource(metaclass=ABCMeta):
    def __init__(self, file_path):
        self.__file_path = file_path

    def parse_file(self):
        with open(self.__file_path, newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            section_name = None

            for row in csv_reader:

                if len(row) > 0:
                    if row[0] in SECTION_HEADERS:
                        section_name = row[0]

                    else:
                        if section_name == ELECTRICAL_APPLIANCES_SECTION_HEADER:
                            if row[0] == ELECTRICAL_APPLIANCES_SECTION_FIRST_COLUMN_NAME:
                                self._handle_electrical_appliances_header_row(row)
                            else:
                                self._handle_electrical_appliances_data_row(row)

                        if section_name == TARIFFS_SECTION_HEADER:
                            if row[0] == TARIFFS_SECTION_FIRST_COLUMN_NAME:
                                self._handle_tariffs_header_row(row)
                            else:
                                self._handle_tariffs_data_row(row)

                        if section_name == HOUSEHOLDS_SECTION_HEADER:
                            if row[0] == HOUSEHOLDS_SECTION_FIRST_COLUMN_NAME:
                                self._handle_households_header_row(row)
                            else:
                                self._handle_households_data_row(row)

    def _handle_electrical_appliances_header_row(self, cells):
        pass

    def _handle_electrical_appliances_data_row(self, cells):
        pass

    def _handle_tariffs_header_row(self, cells):
        pass

    def _handle_tariffs_data_row(self, cells):
        pass

    def _handle_households_header_row(self, cells):
        pass

    def _handle_households_data_row(self, cells):
        pass
