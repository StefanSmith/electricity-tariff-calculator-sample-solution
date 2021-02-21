from decimal import Decimal

from domain.tariff import Tariff


def tariff_with(name='default name', standing_charge_pounds='0', day_unit_cost_pounds_per_kw='0',
                night_unit_cost_pounds_per_kw='0', monthly_discount_kwh_threshold='0', monthly_discount_percent='0'):
    return Tariff(
        name=name,
        standing_charge_pounds=Decimal(standing_charge_pounds),
        day_unit_cost_pounds_per_kw=Decimal(day_unit_cost_pounds_per_kw),
        night_unit_cost_pounds_per_kw=Decimal(night_unit_cost_pounds_per_kw),
        monthly_discount_kwh_threshold=Decimal(monthly_discount_kwh_threshold),
        monthly_discount_percent=Decimal(monthly_discount_percent)
    )
