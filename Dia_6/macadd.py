import getmac
import psutil
import socket
from getmac import getmac

interface = "eth0"
def get_mac_address_of_interface(interface):
    """
    :param interface: The friendly name of a network interface
    :return: the MAC address associated with that interface
    """
    for k,v in psutil.net_if_addrs().items():
        if interface == k:
            for item in v:
                try:
                    if item.family == socket.AF_LINK:
                        return item.address
                except AttributeError:
                    # Linux
                    if item.family == socket.AF_PACKET:
                        return item.address
    return None 