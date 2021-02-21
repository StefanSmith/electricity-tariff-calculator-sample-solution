from decimal import Decimal
from unittest.mock import MagicMock

from domain.cheapest_tariff_report_service import CheapestTariffReportService
from support.builders.appliance_builder import appliance_with
from support.builders.appliance_consumption_builder import appliance_usage_with
from support.builders.household_builder import household_with
from support.builders.tariff_builder import tariff_with


def test_should_report_cheapest_tariff_per_household():
    # given
    tariff_1 = tariff_with(name='Tariff 1', standing_charge_pounds='6.00', day_unit_cost_pounds_per_kw='0.135',
                           night_unit_cost_pounds_per_kw='0.135')

    tariff_2 = tariff_with(name='Tariff 2', standing_charge_pounds='6.30', day_unit_cost_pounds_per_kw='0.150',
                           night_unit_cost_pounds_per_kw='0.120')

    tariff_3 = tariff_with(name='Tariff 3', standing_charge_pounds='6.00', day_unit_cost_pounds_per_kw='0.160',
                           night_unit_cost_pounds_per_kw='0.110')

    tariff_4 = tariff_with(name='Tariff 4', standing_charge_pounds='6.15', day_unit_cost_pounds_per_kw='0.150',
                           night_unit_cost_pounds_per_kw='0.130')

    tariff_source = MagicMock()
    tariff_source.get_tariffs = MagicMock(return_value=[tariff_1, tariff_2, tariff_3, tariff_4])

    display = MagicMock()

    tariff_calculator = CheapestTariffReportService(tariff_source=tariff_source, display=display)

    first_household = household_with(
        monthly_appliance_usage=[
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='500'),
                daytime_hours='12',
                nighttime_hours='8'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='2500'),
                daytime_hours='12',
                nighttime_hours='8'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='70'),
                daytime_hours='16',
                nighttime_hours='60'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='2100'),
                daytime_hours='1',
                nighttime_hours='1'
            )
        ]
    )

    second_household = household_with(
        monthly_appliance_usage=[
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='500'),
                daytime_hours='0',
                nighttime_hours='12'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='2500'),
                daytime_hours='0',
                nighttime_hours='8'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='70'),
                daytime_hours='12',
                nighttime_hours='48'
            ),
            appliance_usage_with(
                appliance=appliance_with(consumption_watts='2100'),
                daytime_hours='1',
                nighttime_hours='2'
            )
        ]
    )

    household_source = MagicMock()
    household_source.get_households = MagicMock(return_value=[first_household, second_household])

    # when
    tariff_calculator.generate_report_for_households_in(household_source)

    # then
    display.render_results.assert_called_once()
    args, kwargs = display.render_results.call_args

    results = args[0]
    assert len(results) == 2

    first_result = results[0]
    assert first_result.household == first_household
    assert first_result.cheapest_tariff == tariff_1
    assert first_result.monthly_cost_pounds == Decimal('15.38520')

    second_result = results[1]
    assert second_result.household == second_household
    assert second_result.cheapest_tariff == tariff_3
    assert second_result.monthly_cost_pounds == Decimal('10.16200')
