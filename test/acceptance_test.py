from support.command_line_utils import run_command
from support.file_utils import absolute_path_to_file


def test_reports_best_tariff_per_household_based_on_provided_data():
    command_result = run_command(
        'python',
        absolute_path_to('..', 'tariff_calculator', 'index.py'),
        absolute_path_to('..', 'input.csv')
    )

    assert command_result.return_code == 0

    assert len(command_result.stdout_lines) == 6

    assert command_result.stdout_lines == [
        'Household,Tariff,Cost (£)',
        'Household A,Tariff 1,45.76',
        'Household B,Tariff 3,38.96',
        'Household C,Tariff 1,46.55',
        'Household D,Tariff 3,43.86',
        '',
    ]


def absolute_path_to(*args):
    return absolute_path_to_file(__file__, *args)
