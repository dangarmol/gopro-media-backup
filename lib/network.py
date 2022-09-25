"""
Static utilities for network related operations.
"""

import re


def parse_mac_address(line: str) -> str:
    """
    Extract a MAC address from a single-line string.
    The MAC address must use colons as separators (e.g. 01:23:45:67:89:AB).

    Arguments:
        - `line` (str): Single line of text to search for a MAC address.

    Raises:
        - `ValueError`: If there is more than one line of text provided as input.

    Returns:
        str: Returns the first MAC address found.
    """

    result = re.search(r"([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})", line)
    return result.group(0) if result else ""
