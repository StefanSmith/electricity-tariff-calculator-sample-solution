from decimal import Decimal

from domain.appliance import Appliance


def appliance_with(consumption_watts='0'):
    return Appliance(Decimal(consumption_watts))


def appliance_with_defaults():
    return appliance_with()
