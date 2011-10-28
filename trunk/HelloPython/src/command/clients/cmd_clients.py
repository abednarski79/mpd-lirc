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

class PlaylistClient():
    
    def __init__(self):
        self.client = RealClient()
        self.playlistManager = PlaylistManager(self.client);
        self.invoker = LoggingInvoker()
        
    def playNextAlbum(self):
        command = PlayNextAlbumCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()    
    
    def playPreviousAlbum(self):
        command = PlayPreviousAlbumCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()
    
    def playNextSong(self):
        command = PlayNextSongCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()
    
    def playPrevious(self):
        command = PlayPreviousSongCommand(self.playlistManager)
        if self.invoker(command) == constants.EX_FAIL:
            self.client.reset()

def main():
    print sys.argv
    playlistClient = PlaylistClient()
    
# Script starts here
if __name__ == "__main__":
    main()  
    
  