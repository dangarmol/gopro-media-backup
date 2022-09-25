from subprocess import Popen, PIPE


def run_command(command: str) -> str:
    """
    Runs the specified command on the current device. This can be useful to perform actions on the Raspberry Pi's when running the scripts on them directly.

    Arguments:
        - `command` (str): The command to be run on the shell.

    Raises:
        - `SystemError`: If there is any content returned via stderr.

    Returns:
        tuple (stdout, stderr): Returns a tuple with the contents of stdout and stderr as bytes after running the command.
    """

    (out, err) = Popen(command, shell=True, stdout=PIPE, stderr=PIPE).communicate()

    if err:
        raise (SystemError(err.decode("utf-8")))

    return out.decode("utf-8")
