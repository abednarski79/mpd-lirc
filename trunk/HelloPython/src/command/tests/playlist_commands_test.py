'''
Created on 8 Oct 2011

@author: abednarski
'''

import unittest
from command.commands.playlist_commands import PlayNextAlbumCommand
from command.commands.playlist_commands import PlayPreviousAlbumCommand
from command.commands.playlist_commands import PlayNextSongCommand
from command.commands.playlist_commands import PlayPreviousSongCommand
import command.utils.constants as constants
import playlist_commands_test_data_1 as data_1
import playlist_commands_test_data_2 as data_2
from command.receivers.playlist_manager import PlaylistManager
from command.utils.client import MockClient

class PlaylistCommandsTest(unittest.TestCase):
    
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        # load playlist_1
        self.playlist_1 = data_1.playlist
        self.playlist_2 = data_2.playlist
    
    def testNextSongWhenCurrentIsNotLast(self):     
        self.currentsong=self.playlist_1[8]   
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(9));
    
    def testNextSongWhenCurrentIsLast(self):
        self.currentsong=self.playlist_1[14]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
    
    def testPreviousSongWhenCurrentIsNotFirst(self):
        self.currentsong=self.playlist_1[8]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(7));
    
    def testPreviousSongWhenCurrentIsFirst(self):
        self.currentsong=self.playlist_1[0]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
        
    def testNextAlbumWhenCurrentIsNotLast(self):
        self.currentsong=self.playlist_1[6]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(9));

    def testNextAlbumWhenCurrentIsLast_1(self):
        self.currentsong=self.playlist_1[14]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
      
    def testNextAlbumWhenCurrentIsLast_2_1(self):
        self.currentsong=self.playlist_2[9]
        client = MockClient(self.currentsong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(12));
  
    def testNextAlbumWhenCurrentIsLast_2_2(self):
        self.currentsong=self.playlist_2[13]
        client = MockClient(self.currentsong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
                
    def testPreviousAlbumWhenCurrentIsNotFirst_1(self):
        self.currentsong=self.playlist_1[8]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(3));
        
    def testPreviousAlbumWhenCurrentIsNotFirst_2(self):
        self.currentsong=self.playlist_2[13]
        client = MockClient(self.currentsong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_OK);
        self.assertEqual(client.currentsong()['pos'], str(9));
        
    def testPreviousAlbumWhenCurrentIsFirst(self):
        self.currentsong=self.playlist_1[2]
        client = MockClient(self.currentsong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        result = command.execute()
        self.assertEqual(result, constants.EX_FAIL);
            