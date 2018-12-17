#!/usr/bin/python3

# **********************************************************************
#  Project           : 6LOWPAN ON RASPBERRYPI (RPI)
#
#  Program name      : temp_server.py
#
#  Description       : Program for a flask server asking the temp to a sensor
#                      and renderit in a HTML file
#
#  Author            : Carlos Hansen and Mustafa Khaan Claasz Coockson
#
# **********************************************************************

from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)
app.debug = True


@app.route("/")
def temp():
    # specify the IPv6 "scope id" to make sure it uses the 6LoWPAN network
    scope_id = socket.if_nametoindex('lowpan0')
    # Create the socket with a IPv6 address family socket for the for the SOCK_DGRAM type
    sock_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, 0)

    # Send the encoded message
    sock_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, 0)

    # Set the socket to recv mode and wait for the answer
    data = sock_ipv6.recv(1024)  # buffer size
    return render_template('temp.html', message=data.decode('utf-8'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
