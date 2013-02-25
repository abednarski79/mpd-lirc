#!/usr/bin/python

# usage: send_and_receive_arduino <DEVICE> <BAUDRATE> # <TEXT>
# where <DEVICE> is typically some /dev/ttyfoobar
# and where <BAUDRATE> is the baudrate
## and where <TEXT> is a text, e.g. "Hello"

import sys
import serial
import time
import subprocess
port = sys.argv[1]
baudrate = sys.argv[2]
print "Initializeing serial port: " + port + " " + baudrate
ser = serial.Serial()
ser.port = port
ser.baudrate = baudrate
ser.open()
while 1:
	output = ser.readline()
	print output
	if output.startswith("4,"):
		powerOffCommand = "/root/scripts/mpd_v2/commands/powerOff/powerOffSingleRunWrapper.sh" 
		print powerOffCommand
		subprocess.call([powerOffCommand])
		# relayOffCommand = "echo" 
		# relayOffParameters = "\"12,120000;\" > " + port
		# print relayOffCommand
		# subprocess.call([relayOffCommand, relayOffParameters])

