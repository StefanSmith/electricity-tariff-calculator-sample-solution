from decimal import Decimal

from support.builders.tariff_builder import tariff_with


def test_should_include_standing_charge_in_monthly_cost():
    tariff = tariff_with(standing_charge_pounds='5.00')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('0'),
                                                  nighttime_consumption_kwh=Decimal('0'))

    assert monthly_cost == Decimal('5.00')


def test_should_include_daytime_consumption_in_monthly_cost():
    tariff = tariff_with(standing_charge_pounds='0', day_unit_cost_pounds_per_kw='0.34')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('10'),
                                                  nighttime_consumption_kwh=Decimal('0'))

    assert monthly_cost == Decimal('3.40')


def test_should_include_nighttime_consumption_in_monthly_cost():
    tariff = tariff_with(standing_charge_pounds='0', night_unit_cost_pounds_per_kw='0.56')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('0'),
                                                  nighttime_consumption_kwh=Decimal('10'))

    assert monthly_cost == Decimal('5.60')


def test_should_discount_consumption_above_threshold():
    tariff = tariff_with(standing_charge_pounds='0', day_unit_cost_pounds_per_kw='0.20',
                         night_unit_cost_pounds_per_kw='0.10', monthly_discount_kwh_threshold='200',
                         monthly_discount_percent='10.00')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('150'),
                                                  nighttime_consumption_kwh=Decimal('150'))

    assert monthly_cost == Decimal('43.5')


def test_should_not_discount_standing_charge():
    tariff = tariff_with(standing_charge_pounds='5.00', day_unit_cost_pounds_per_kw='0.20',
                         night_unit_cost_pounds_per_kw='0.10', monthly_discount_kwh_threshold='200',
                         monthly_discount_percent='10.00')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('150'),
                                                  nighttime_consumption_kwh=Decimal('150'))

    assert monthly_cost == Decimal('48.5')


def test_should_support_zero_consumption():
    tariff = tariff_with(standing_charge_pounds='10.00')

    monthly_cost = tariff.get_monthly_cost_pounds(daytime_consumption_kwh=Decimal('0'),
                                                  nighttime_consumption_kwh=Decimal('0'))

    assert monthly_cost == Decimal('10.00')
