"""
Functions to enable Bluetooth functionality on the Raspberry Pi, pair with the GoPro
and enable the GoPro wi-fi access point.
"""


from subprocess import Popen, PIPE

from shell import run_command
from network import parse_mac_address


class Bluetooth:
    # bluetoothctl + gatttool

    def __init__(self):
        self._devices = {}  # {"GoPro 1234": "01:23:45:67:89:AB"}
        self._selected_device = None | str

    @staticmethod
    def power(switch_on=True) -> None:
        """
        bluetooth power on/off
        """

        run_command(f"bluetoothctl power {'on' if switch_on else 'off'}")

    def scan_for_devices(self, timeout_s=5) -> None:
        """
        timeout 5 bluetoothctl scan on
        """

        run_command(f"timeout {timeout_s} bluetoothctl scan on")
        self.__parse_gopro_devices()

    def list_gopro_devices(self) -> list:
        """
        Return a list of GoPro devices available for connection via Bluetooth.
        """
        return list(self._devices.keys())

    def select_device(self, device_id: str) -> None:
        """
        Marks a device as selected to perform subsequent operations on it.
        """
        if device_id not in self._devices:
            raise ValueError(
                "The specified ID could is not in the list of found devices."
            )
        self._selected_device = device_id

    def pair_device(self) -> None:
        """
        bluetoothctl pair 01:23:45:67:89:AB
        """

        """
        pi@raspi0hbg-01:~ $ bluetoothctl pair CB:88:55:AA:AA:CA
        Failed to pair: org.bluez.Error.AuthenticationCanceled
        pi@raspi0hbg-01:~ $ bluetoothctl pair CB:88:55:AA:AA:CA
        Attempting to pair with CB:88:55:AA:AA:CA
        [CHG] Device CB:88:55:AA:AA:CA Connected: yes
        [CHG] Device CB:88:55:AA:AA:CA Paired: yes
        Pairing successful
        """
        if self._selected_device is None:
            raise ValueError(
                "You must select a device before performing this operation. \
                    Use Bluetooth.select_device()."
            )
        print(run_command(f"bluetoothctl pair {self._devices[self._selected_device]}"))

    def trust_device(self) -> None:
        """
        bluetoothctl trust 01:23:45:67:89:AB
        """

        if self._selected_device is None:
            raise ValueError(
                "You must select a device before performing this operation. \
                    Use Bluetooth.select_device()."
            )
        print(run_command(f"bluetoothctl trust {self._devices[self._selected_device]}"))

    def connect_to_gopro_ble(self):
        pass

    def send_ble_write_request(self):
        pass

    def __parse_gopro_devices(self) -> None:
        """
        bluetoothctl devices | grep -i gopro
        """

        devices = {}
        output = run_command("bluetoothctl devices | grep -i gopro")
        for line in output.splitlines():
            mac_addr = parse_mac_address(line)
            if mac_addr:
                device_name = line.split(mac_addr)[-1].strip()
                devices[device_name] = mac_addr
        self._devices = devices
