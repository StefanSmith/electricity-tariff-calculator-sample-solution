from decimal import Decimal

from integration.csv_file.csv_file_household_source import CsvFileHouseholdSource
from support.file_utils import absolute_path_to_file


def test_should_provide_tariffs_parsed_from_tariff_calculator_csv_input_file():
    # given
    household_source = CsvFileHouseholdSource(absolute_path_to_file(__file__, '..', '..', '..', '..', 'input.csv'))

    # when
    households = household_source.get_households()

    # then
    first_household = households[0]
    assert first_household.name == 'Household A'
    assert first_household.monthly_kwh == (Decimal('147.42'), Decimal('149.3'))

    second_household = households[1]
    assert second_household.name == 'Household B'
    assert second_household.monthly_kwh == (Decimal('100.24'), Decimal('153.86'))

    third_household = households[2]
    assert third_household.name == 'Household C'
    assert third_household.monthly_kwh == (Decimal('166.38'), Decimal('136.78'))
