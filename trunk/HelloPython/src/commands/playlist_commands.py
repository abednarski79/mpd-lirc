'''
Created on 11 Oct 2011

@author: abednarski
'''
import command_interface
import receivers

class PlayNextAlbumCommand(command_interface.Command):
    """The Command class for playing next album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = receivers.playlist_manager.PlaylistManager
    def execute(self):
            self.__playlistManager.playNextAlbum()

class PlayPreviousAlbumCommand(command_interface.Command):
    """The Command class for playing pevious album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = receivers.playlist_manager.PlaylistManager
    def execute(self):
            self.__playlistManager.playPreviousAlbum()

class PlayNextSongCommand(command_interface.Command):
    """The Command class for playing next album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = receivers.playlist_manager.PlaylistManager
    def execute(self):
            self.__playlistManager.playNextSong()

class PlayPreviousSongCommand(command_interface.Command):
    """The Command class for playing previous album"""
    def __init__(self,playlist_manager):
            self.__playlistManager = receivers.playlist_manager.PlaylistManager
    def execute(self):
            self.__playlistManager.playPreviousSong()            