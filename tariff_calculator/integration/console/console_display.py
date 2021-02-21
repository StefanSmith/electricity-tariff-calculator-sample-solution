class ConsoleDisplay:
    def render_results(self, results):
        self.__render_text('\n'.join(
            [
                'Household,Tariff,Cost (£)',
                *[self.__render_result(result) for result in results]
            ]))

    @staticmethod
    def __render_result(household_result):
        return ','.join([
            household_result.household.name,
            household_result.cheapest_tariff.name,
            f'{household_result.monthly_cost_pounds:.2f}'
        ])

    @staticmethod
    def __render_text(text):
        print(text)
