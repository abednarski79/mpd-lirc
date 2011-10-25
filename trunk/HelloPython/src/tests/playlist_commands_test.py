'''
Created on 8 Oct 2011

@author: abednarski
'''

import unittest
from commands.playlist_commands import PlayNextAlbumCommand
from commands.playlist_commands import PlayPreviousAlbumCommand
from commands.playlist_commands import PlayNextSongCommand
from commands.playlist_commands import PlayPreviousSongCommand
import utils.constants as constants
import playlist_commands_test_data as data
from receivers.playlist_manager import PlaylistManager
from utils.client import MockClient

class PlaylistManagerTest(unittest.TestCase):
    
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        # load playlist
        self.playlist = data.playlist
    
    def testNextSongWhenCurrentIsNotLast(self):     
        self.currentsong=self.playlist[8]   
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(9));
    
    def testNextSongWhenCurrentIsLast(self):
        self.currentsong=self.playlist[14]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
    
    def testPreviousSongWhenCurrentIsNotFirst(self):
        self.currentsong=self.playlist[8]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(7));
    
    def testPreviousSongWhenCurrentIsFirst(self):
        self.currentsong=self.playlist[0]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
        
    def testNextAlbumWhenCurrentIsNotLast(self):
        self.currentsong=self.playlist[6]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(9));

    def testNextAlbumWhenCurrentIsLast(self):
        self.currentsong=self.playlist[14]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);

    def testPreviousAlbumWhenCurrentIsNotFirst(self):
        self.currentsong=self.playlist[8]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(3));
        
    def testPreviousAlbumWhenCurrentIsFirst(self):
        self.currentsong=self.playlist[2]
        client = MockClient(self.currentsong, self.playlist)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
            