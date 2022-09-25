"""
Static functions to run shell commands.
"""


from subprocess import Popen, PIPE


def run_command(command: str) -> str:
    """
    Runs the specified command on the current device default shell.

    Arguments:
        - `command` (str): Command to be run.

    Raises:
        - `SystemError`: If there is any content returned via stderr.

    Returns:
        str: Contents of stdout after running the command, decoded using current locale.
    """

    (out, err) = Popen(command, shell=True, stdout=PIPE, stderr=PIPE).communicate()

    if err:
        raise (SystemError(err.decode("utf-8")))

    return out.decode("utf-8")
