#!/usr/bin/python3

# **********************************************************************
#  Project           : 6LOWPAN ON RASPBERRYPI (RPI)
#
#  Program name      : sink_udp.py
#
#  Description       : Program to ask for a temperature to a sensor via
#                      6LowPan over UDP
#
#  Author            : Carlos Hansen and Mustafa Khaan Claasz Coockson
#
# **********************************************************************

import socket
import time

UDP_IP = '2001:db8::2'      # IP address of the Sensor for UDP comm 
PORT = 1500

def main():
    # specify the IPv6 "scope id" to make sure it uses the 6LoWPAN network
    scope_id = socket.if_nametoindex('lowpan0')
    while True:
        # Create the socket with a IPv6 address family socket for the for the SOCK_DGRAM type
        sock_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, 0)
        
        # Send the encoded message
        sock_ipv6.sendto(b" ", (UDP_IP, PORT, 0, scope_id))
        
        # Set the socket to recv mode and wait for the answer
        data = sock_ipv6.recv(1024) # buffer size
        print(data.decode('utf-8'))
        time.sleep(5)

if __name__ == '__main__':
    main()