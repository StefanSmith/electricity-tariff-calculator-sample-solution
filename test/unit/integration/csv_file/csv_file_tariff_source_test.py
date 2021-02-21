from decimal import Decimal

from integration.csv_file.csv_file_tariff_source import CsvFileTariffSource
from support.file_utils import absolute_path_to_file


def test_should_provide_tariffs_parsed_from_tariff_calculator_csv_input_file():
    # given
    tariff_source = CsvFileTariffSource(absolute_path_to_file(__file__, '..', '..', '..', '..', 'input.csv'))

    # when
    tariffs = tariff_source.get_tariffs()

    # then
    first_tariff = tariffs[0]
    assert first_tariff.name == 'Tariff 1'
    assert first_tariff.get_monthly_cost_pounds(0, 0) == Decimal('6.00')
    assert first_tariff.get_monthly_cost_pounds(1, 0) == Decimal('6.135')
    assert first_tariff.get_monthly_cost_pounds(0, 1) == Decimal('6.135')

    second_tariff = tariffs[1]
    assert second_tariff.name == 'Tariff 2'
    assert second_tariff.get_monthly_cost_pounds(0, 0) == Decimal('6.30')
    assert second_tariff.get_monthly_cost_pounds(1, 0) == Decimal('6.450')
    assert second_tariff.get_monthly_cost_pounds(0, 1) == Decimal('6.420')

    third_tariff = tariffs[2]
    assert third_tariff.name == 'Tariff 3'
    assert third_tariff.get_monthly_cost_pounds(0, 0) == Decimal('6.00')
    assert third_tariff.get_monthly_cost_pounds(1, 0) == Decimal('6.160')
    assert third_tariff.get_monthly_cost_pounds(0, 1) == Decimal('6.110')


def test_should_parse_tariff_discount_threshold_and_percentage_from_file():
    # given
    tariff_source = CsvFileTariffSource(absolute_path_to_file(__file__, '..', '..', '..', '..', 'input.csv'))

    # when
    tariffs = tariff_source.get_tariffs()

    # then
    first_tariff = tariffs[0]
    assert first_tariff.name == 'Tariff 1'
    assert first_tariff.get_monthly_cost_pounds(Decimal('200'), Decimal('200')) == Decimal('58.3125')
