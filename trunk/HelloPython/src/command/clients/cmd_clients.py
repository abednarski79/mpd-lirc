'''
Created on 28 Oct 2011

@author: abednarski
'''

from command.commands.playlist_commands import PlayNextAlbumCommand
from command.commands.playlist_commands import PlayPreviousAlbumCommand
from command.commands.playlist_commands import PlayNextSongCommand
from command.commands.playlist_commands import PlayPreviousSongCommand
import command.utils.constants as constants
from command.receivers.playlist_manager import PlaylistManager
from command.utils.client import RealClient
from command.invokers.invokers import LoggingInvoker
import sys
import os

PLAY_NEXT_ALBUM = "PLAY_NEXT_ALBUM"
PLAY_PREVIOUS_ALBUM = "PLAY_PREVIOUS_ALBUM"
PLAY_NEXT_SONG = "PLAY_NEXT_SONG"
PLAY_PREVIOUS_SONG = "PLAY_PREVIOUS_SONG"
VALID_COMMAND_CODES = [PLAY_NEXT_ALBUM, PLAY_PREVIOUS_ALBUM, PLAY_NEXT_SONG, PLAY_PREVIOUS_SONG]

class PlaylistClient():    
    
    def __init__(self):
        self.client = RealClient()
        self.playlistManager = PlaylistManager(self.client);
        self.invoker = LoggingInvoker()
        
    def playNextAlbum(self):
        command = PlayNextAlbumCommand(self.playlistManager)
        self.invoker.setCommand(command)
        if self.invoker.executeCommand() == constants.EX_FAIL:
            self.client.reset()    
    
    def playPreviousAlbum(self):
        command = PlayPreviousAlbumCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()
    
    def playNextSong(self):
        command = PlayNextSongCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()
    
    def playPreviousSong(self):
        command = PlayPreviousSongCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()

def validateCommandLineParameter(commandLineParameter):
    if(len(commandLineParameter) < 2 or 
       commandLineParameter[1] is None or 
       len(commandLineParameter[1]) == 0 or 
       commandLineParameter[1] not in VALID_COMMAND_CODES):
        errorMessage = "Please provide one of the valid parameters: " + str(VALID_COMMAND_CODES)
        sys.exit(errorMessage)

def executeCommand(playlistClient, commandCode):
    if(commandCode == PLAY_NEXT_ALBUM):
        playlistClient.playNextAlbum()
    elif(commandCode == PLAY_PREVIOUS_ALBUM):
        playlistClient.playPreviousAlbum()
    elif(commandCode == PLAY_NEXT_SONG):
        playlistClient.playNextSong()
    elif(commandCode == PLAY_PREVIOUS_SONG):
        playlistClient.playPreviousSong()    

def main():
    playlistClient = PlaylistClient()
    validateCommandLineParameter(sys.argv)
    commandCode = sys.argv[1]
    executeCommand(playlistClient, commandCode)
    
# Script starts here
if __name__ == "__main__":
    main()  
    
  