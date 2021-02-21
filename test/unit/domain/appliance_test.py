from decimal import Decimal

from support.builders.appliance_builder import appliance_with


def test_should_calculate_kwh_consumption_for_specified_hours_usage():
    # given
    appliance = appliance_with(consumption_watts=400)

    # when
    kwh_consumption = appliance.get_kwh_consumed(15)

    # then
    assert kwh_consumption == Decimal('6')
