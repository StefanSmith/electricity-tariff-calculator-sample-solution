from decimal import Decimal
from unittest.mock import MagicMock

from domain.tariff_calculator import TariffCalculator
from support.builders.appliance_builder import appliance_with
from support.builders.appliance_consumption_builder import appliance_usage_with, default_appliance_usage
from support.builders.household_builder import household_with, default_household
from support.builders.tariff_builder import tariff_with


def test_should_determine_cheapest_tariff_for_a_household():
    # given
    tariff_1 = tariff_with(name='Tariff 1', standing_charge_pounds='2')
    tariff_2 = tariff_with(name='Tariff 2', standing_charge_pounds='1')
    tariff_3 = tariff_with(name='Tariff 3', standing_charge_pounds='3')

    tariff_source = MagicMock()
    tariff_source.get_tariffs = MagicMock(return_value=[tariff_1, tariff_2, tariff_3])

    tariff_calculator = TariffCalculator(tariff_source=tariff_source)

    household = default_household()

    # when
    result = tariff_calculator.determine_cheapest_tariff_for(household)

    # then
    assert result.household == household
    assert result.cheapest_tariff == tariff_2


def test_should_consider_daytime_consumption_when_determining_cheapest_tariff_for_a_household():
    # given
    tariff_1 = tariff_with(name='Tariff 1', standing_charge_pounds='0', day_unit_cost_pounds_per_kw='2')
    tariff_2 = tariff_with(name='Tariff 2', standing_charge_pounds='0', day_unit_cost_pounds_per_kw='1')
    tariff_3 = tariff_with(name='Tariff 3', standing_charge_pounds='0', day_unit_cost_pounds_per_kw='3')

    tariff_source = MagicMock()
    tariff_source.get_tariffs = MagicMock(return_value=[tariff_1, tariff_2, tariff_3])

    tariff_calculator = TariffCalculator(tariff_source=tariff_source)

    household = household_with(
        monthly_appliance_usage=[
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='1000'),
                daytime_hours='1',
                nighttime_hours='0'
            )
        ]
    )

    # when
    result = tariff_calculator.determine_cheapest_tariff_for(household)

    # then
    assert result.household == household
    assert result.cheapest_tariff == tariff_2
    assert result.monthly_cost_pounds == Decimal('1.00')


def test_should_consider_nighttime_consumption_when_determining_cheapest_tariff_for_a_household():
    # given
    tariff_1 = tariff_with(name='Tariff 1', standing_charge_pounds='0', night_unit_cost_pounds_per_kw='2')
    tariff_2 = tariff_with(name='Tariff 2', standing_charge_pounds='0', night_unit_cost_pounds_per_kw='1')
    tariff_3 = tariff_with(name='Tariff 3', standing_charge_pounds='0', night_unit_cost_pounds_per_kw='3')

    tariff_source = MagicMock()
    tariff_source.get_tariffs = MagicMock(return_value=[tariff_1, tariff_2, tariff_3])

    tariff_calculator = TariffCalculator(tariff_source=tariff_source)

    household = household_with(
        monthly_appliance_usage=[
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='1000'),
                daytime_hours='0',
                nighttime_hours='1'
            )
        ]
    )

    # when
    result = tariff_calculator.determine_cheapest_tariff_for(household)

    # then
    assert result.household == household
    assert result.cheapest_tariff == tariff_2
    assert result.monthly_cost_pounds == Decimal('1.00')
