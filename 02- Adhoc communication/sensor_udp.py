#!/usr/bin/python3

# **********************************************************************
#  Project           : 6LOWPAN ON RASPBERRYPI (RPI)
#
#  Program name      : sensor_udp.py
#
#  Description       : Program to answer for a temperature to a sensor via
#                      6LowPan over UDP
#
#  Author            : Carlos Hansen and Mustafa Khaan Claasz Coockson
#
# **********************************************************************

import socket
from subprocess import PIPE, Popen
import time

HOST = ''           # Name to set all available interfaces
UDP_PORT = 1500     # Arbitrary non-privileged port


def get_cpu_temperature():
    """Function to get the temperature of the CPU"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return output


def main():
    # Create the socket with a IPv6 address family socket for the for the SOCK_DGRAM type
    sock_ipv6 = socket.socket(socket.AF_INET6,         # Ipv6
                       socket.SOCK_DGRAM, 0)    # UDP

    # specify the IPv6 "scope id" to make sure it uses the 6LoWPAN network
    scope_id = socket.if_nametoindex('lowpan0')

    # Bind the socket
    sock_ipv6.bind((HOST, UDP_PORT, 0, scope_id))

    print("Accepting data requests...")

    while True:
        # Accept a connection.
        # Return (data, address)
        # data from the connection,
        # address is the address bound to the socket on the other end of the connection.
        data, address = sock_ipv6.recvfrom(1024)

        # return the Temperature 
        sock_ipv6.sendto(get_cpu_temperature(), address)


if __name__ == '__main__':
    main()
