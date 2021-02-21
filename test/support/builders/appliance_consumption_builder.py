from decimal import Decimal

from domain.appliance_usage import ApplianceUsage
from support.builders.appliance_builder import appliance_with_defaults


def appliance_usage_with(appliance=None, daytime_hours='0', nighttime_hours='0'):
    if appliance is None:
        appliance = appliance_with_defaults()

    return ApplianceUsage(appliance=appliance, daytime_hours=Decimal(daytime_hours),
                          nighttime_hours=Decimal(nighttime_hours))


def default_appliance_usage():
    return appliance_usage_with()
