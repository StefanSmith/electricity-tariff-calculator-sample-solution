from domain.household import Household


def household_with(name='default name', monthly_appliance_usage=None):
    if monthly_appliance_usage is None:
        monthly_appliance_usage = []

    return Household(name=name, monthly_appliance_usage=monthly_appliance_usage)


def default_household():
    return household_with()
