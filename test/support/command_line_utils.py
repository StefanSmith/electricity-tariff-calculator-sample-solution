import subprocess
from logging import getLogger

LOGGER = getLogger(__name__)


class CommandResult:

    def __init__(self, completed_process):
        self.return_code = completed_process.returncode
        self.stdout_lines = completed_process.stdout.split('\n')


def run_command(command, *command_arguments):
    completed_process = subprocess.run(
        args=(command,) + command_arguments,
        capture_output=True,
        timeout=10,
        text=True
    )

    if len(completed_process.stderr) > 0:
        LOGGER.error('Process wrote to stderr:\n' + completed_process.stderr)

    if len(completed_process.stdout) > 0:
        LOGGER.info('Process wrote to stdout:\n' + completed_process.stdout)

    return CommandResult(completed_process)
