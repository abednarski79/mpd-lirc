'''
Created on 20 Oct 2011

@author: abednarski
'''

from client_interface import Client
from command.utils.connection_utils import ConnectionManager

class MockClient(Client):
    
    def __init__(self, current, plist):
        print "Initializing MockClient"
        self.current = current
        self.plist = plist
        
    def currentsong(self):
        print "Current song position: ", self.current['pos']
        return self.current
    
    def playlistid(self, position):
        print "Searching song with position: ", position
        if position < 0:
            print "Song not found, position index less then zero"
            return None
        if position > (len(self.plist) - 1):
            print "Song not found, position index exides playlist size"
            return None
        print "Song found at position: ", position
        return self.plist[position]
    
    def play(self, position):
        print "Playing song at position: ", position
        self.current = self.plist[position]


class RealClient(Client):
    
    def __init__(self):
        print "Initializing RealClient"
        self.connectionManager = ConnectionManager()
        self.client = self.connectionManager.getClient()
        
    def reset(self):
        self.play(0)
        
    def next(self):
        print "Skiping to previous song"
        self.client.next()
    
    def previous(self):
        print "Skiping to next song"
        self.client.next()
    
    def currentsong(self):
        print "Retrieving current song"
        return self.client.currentsong()
    
    def playlistid(self, position):
        print "Searching song with position: ", position
        return self.client.playlistid(position)
    
    def play(self, position):
        print "Playing song at position: ", position
        self.client.play(position)
