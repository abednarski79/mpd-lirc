#!/usr/bin/python

import pylirc, time, select
from threading import Thread, Timer 

blocking = 0;
code = ""
t1 = None
isRunning = 1
repeat = None
lastCommand = None
currentCommand = None
clickWaitTime = 0.11
currentModeMappings = None
powerOffRequiredRepeat = 5;

def nextRadioStation():
    print "next radio station"

def previousRadioStation():
    print "previous radio station"

def nextPlayList():
	print "next playlist"

def previousPlayList():
	print "next playlist"

def nextSong():
	print "next song"

def previousSong():
	print "previous song"

def seekForwardSong():
	print "seekForwardSong"

def seekReverseSong():
	print "seekReverseSong"
	
def powerOff():
	print "Power off"

def radioMenu():
	global currentModeMappings
	global playerMappings
	currentModeMappings = playerMappings
	print "radio menu"
		

def playerMenu():
	global currentModeMappings
	global radioMappings
	currentModeMappings = radioMappings
	print "player menu"

def volumeUp():
	print "volume up"

def volumeDown():
	print "volume down"

def notAvailable():
	print "not available"

def playPauseRadio():
	print "play/pause radio"

def playPausePlayer():
	print "play/pause palyer"

def powerOff():
	global repeat
	global isRunning
	if(repeat > powerOffRequiredRepeat):
		print "powerOff"
		isRunning = 0

volumeUpMappings = {'SHORT': volumeUp, 'LONG': volumeUp}
volumeDownMappings = {'SHORT': volumeDown, 'LONG': volumeDown}
commonMappings = {'PLUS': volumeUpMappings, 'MINUS': volumeDownMappings}

nextRadioStationMappings = {'SHORT': nextRadioStation, 'LONG': notAvailable}
previousRadioStationMappings = {'SHORT': previousRadioStation, 'LONG': notAvailable}	
radioMenuMappings = {'SHORT': radioMenu, 'LONG': notAvailable}	
radioPlayPauseMappings = {'SHORT': playPauseRadio, 'LONG': powerOff}
radioMappings = {'FORWARD': nextRadioStationMappings, 'REVERSE': previousRadioStationMappings, 'MENU': radioMenuMappings, 'PLAY': radioPlayPauseMappings}
radioMappings.update(commonMappings)

nextPlayerMappings = {'SHORT': nextSong, 'LONG': seekForwardSong}
previousPlayerMappings = {'SHORT': previousSong, 'LONG': seekReverseSong}
playerMenuMappings = {'SHORT': playerMenu, 'LONG': notAvailable}
playerPlayPauseMappings = {'SHORT': playPausePlayer, 'LONG': powerOff}
playerMappings = {'FORWARD': nextPlayerMappings, 'REVERSE': previousPlayerMappings, 'MENU': playerMenuMappings, 'PLAY': playerPlayPauseMappings}
playerMappings.update(commonMappings)

currentModeMappings = radioMappings

lirchandle = pylirc.init("pylirc", "./conf", blocking)
if(lirchandle):
	input = [lirchandle]
	print "Succesfully opened lirc, handle is " + str(lirchandle)
	while isRunning:
		inputready,outputready,exceptready = select.select(input,[],[])
		s = pylirc.nextcode(1)
		if(s):
			for code in s:
				repeat = code["repeat"]
				currentCommand = code["config"]
				print "Command %s, repleat %s" % (currentCommand, repeat)
				if(repeat == 0):
					# print "Initial click"
					t1 = Timer(clickWaitTime, currentModeMappings[currentCommand]['SHORT'])
					t1.start()
				if(repeat > 0):
					# print "Repeated click"
					t1.cancel()
					currentModeMappings[currentCommand]['LONG']()
				lastCommand = currentCommand
pylirc.exit()