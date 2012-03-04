'''
Created on 20 Oct 2011

@author: abednarski
'''

from client_interface import Client
from command.utils.connection_utils import ConnectionManager
from mpd import CommandError

class MockClient(Client):
    
    def __init__(self, current, plist):
        print "Initializing MockClient"
        self.current = current
        self.plist = plist
        
    def getCurrentSong(self):
        print "Current song position: ", self.current['pos']
        if(self.current is None):
            raise CommandError("Song not found, position index less then zero")
        return self.current
    
    def findSongAtPosition(self, position):
        print "Searching song at position: ", position
        if position < 0:
            raise CommandError("Song not found, position index less then zero")
        if position > (len(self.plist) - 1):
            raise CommandError("Song not found, position index less then zero")
        print "Song found at position: ", position
        return self.plist[position]
    
    def playSongAtPosition(self, position):
        print "Playing song at position: ", position
        if position < 0:
            raise CommandError("Song not found, position index less then zero")
        if position > (len(self.plist) - 1):
            raise CommandError("Song not found, position index less then zero")
        self.current = self.plist[position]


class RealClient(Client):
    
    def __init__(self):
        print "RealClient: Initializing RealClient"
        self.connectionManager = ConnectionManager()
        self.client = self.connectionManager.getClient()
        
    def reset(self):
        print "RealClient: Reseting"
        self.client.play(0)
        
    def goToNextSong(self):
        print "RealClient: Skipping to goToPreviousSong song"
        self.client.next()
    
    def goToPreviousSong(self):
        print "RealClient: Skipping to goToNextSong song"
        self.client.previous()
    
    def getCurrentSong(self):
        print "RealClient: Retrieving current song"
        return self.client.currentsong()
    
    def findSongAtPosition(self, position):
        print "RealClient: Searching song at position: ", position
        if position < 0:
            raise CommandError("Song not found, position index less then zero")
        song = None
        playlist = self.client.playlistinfo(int(position))
        if playlist is not None and len(playlist) > 0:
            song = playlist[0]
        if song is None:
            raise CommandError("Song not found")
        return song
    
    def playSongAtPosition(self, position):
        print "RealClient: Playing song at position: ", position
        self.client.play(position)
