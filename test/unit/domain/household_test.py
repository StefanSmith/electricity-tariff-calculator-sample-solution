from decimal import Decimal

from support.builders.appliance_builder import appliance_with
from support.builders.appliance_consumption_builder import appliance_usage_with
from support.builders.household_builder import household_with


def test_should_calculate_day_and_night_kwh_used_by_specified_appliances_based_on_their_usage_and_power_consumption():
    # given
    household = household_with(monthly_appliance_usage=[
        appliance_usage_with(
            appliance=appliance_with(consumption_watts='300'),
            daytime_hours='5',
            nighttime_hours='3'
        )
    ])

    # when
    daytime_kwh, nighttime_kwh = household.monthly_kwh

    # then
    assert daytime_kwh == Decimal('1.5')
    assert nighttime_kwh == Decimal('0.9')


def test_should_aggregate_consumption_across_all_appliances():
    # given
    household = household_with(monthly_appliance_usage=[
        appliance_usage_with(appliance=appliance_with(consumption_watts='300'),
                             daytime_hours='5', nighttime_hours='3'),
        appliance_usage_with(appliance=appliance_with(consumption_watts='500'),
                             daytime_hours='6', nighttime_hours='10')
    ])

    # when
    daytime_kwh, nighttime_kwh = household.monthly_kwh

    # then
    assert daytime_kwh == Decimal('4.5')
    assert nighttime_kwh == Decimal('5.9')
