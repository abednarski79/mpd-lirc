'''
Created on 11 Oct 2011

@author: abednarski
'''
from command_interface import Command

class PlayNextSongCommand(Command):
    """The Command class for playing next album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = playlist_manager
    def execute(self):
            return self.__playlistManager.playNextSong()

class PlayPreviousSongCommand(Command):
    """The Command class for playing previous album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = playlist_manager
    def execute(self):
            return self.__playlistManager.playPreviousSong()
     
class PlayNextAlbumCommand(Command):
    """The Command class for playing next album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = playlist_manager
    def execute(self):
            print "Calling play next album command"
            return self.__playlistManager.playNextAlbum()

class PlayPreviousAlbumCommand(Command):
    """The Command class for playing pevious album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = playlist_manager
    def execute(self):
        print "Calling previous album command"
        return self.__playlistManager.playPreviousAlbum()