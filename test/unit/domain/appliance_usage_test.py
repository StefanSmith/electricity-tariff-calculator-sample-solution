from decimal import Decimal

from support.builders.appliance_builder import appliance_with
from support.builders.appliance_consumption_builder import appliance_usage_with


def test_should_provide_daytime_kwh_consumption_based_on_appliance_power_and_daytime_hours_used():
    # given
    appliance_usage = appliance_usage_with(
        appliance=appliance_with(consumption_watts='250'),
        daytime_hours='50'
    )

    # when
    daytime_kwh = appliance_usage.daytime_kwh

    # then
    assert daytime_kwh == Decimal('12.5')


def test_should_provide_nighttime_kwh_consumption_based_on_appliance_power_and_nighttime_hours_used():
    # given
    appliance_usage = appliance_usage_with(
        appliance=appliance_with(consumption_watts='250'),
        nighttime_hours='10'
    )

    # when
    nighttime_kwh = appliance_usage.nighttime_kwh

    # then
    assert nighttime_kwh == Decimal('2.5')
