#!/usr/bin/env python3
# encoding=UTF-8
"""
### SharkWrappyr ###
This script is a python wrapper for tshark that takes a pcap and filters
and returns the filtered pcap. Requires tshark to be installed.

Usage: filtered_pcap = shark_wrappyr(pcap_in, pcap_filters)
"""
import subprocess
import sys
import os


print("Starting SharkWrappyr")

# Add Wireshark program folder to PATH
if sys.platform == 'win32':
    # In order to make sure tshark is in the windows PATH
    os.environ['PATH'] += ';C:\Program Files\Wireshark'

# Print tshark version or else error out
try:
    version_message = subprocess.Popen(
        ['tshark', '-v'], stdout=subprocess.PIPE).communicate()[0]
    # version message includes license, so let's take first line
    print(version_message.splitlines()[0].decode("UTF-8"))

# If the tshark executable doesn't exist or isn't on path
except FileNotFoundError:
    print("ERROR: Tshark is not installed"
          "\nOn some OSes, it comes bundled with Wireshark.")


def shark_wrappyr(pcap_in, pcap_filters):
    """
    :arg: Pcap file, pcap filters
    :return: Output pcap file
    """
    pcap_out, ext = os.path.basename(pcap_in).split('.')
    pcap_out += '-out.' + ext
    print("Input file: ", pcap_out, "\nFilters: ", pcap_filters)
    subprocess.call(
        ['tshark', '-n', '-r', pcap_in, '-Y', pcap_filters, '-w', pcap_out],
        shell=True)