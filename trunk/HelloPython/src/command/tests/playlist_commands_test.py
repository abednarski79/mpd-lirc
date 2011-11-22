'''
Created on 8 Oct 2011

@author: abednarski
'''

from command.commands.playlist_commands import PlayNextAlbumCommand, \
    PlayNextSongCommand, PlayPreviousAlbumCommand, PlayPreviousSongCommand
from command.receivers.playlist_manager import PlaylistManager, \
    PlaylistManagerException
from command.utils.client import MockClient
import playlist_commands_test_data_1 as data_1
import playlist_commands_test_data_2 as data_2
import unittest

class PlaylistCommandsTest(unittest.TestCase):
    
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        # load playlist_1
        self.playlist_1 = data_1.playlist
        self.playlist_2 = data_2.playlist
    
    def testNextSongWhenCurrentIsNotLast(self):     
        self.getCurrentSong=self.playlist_1[8]   
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(9));
    
    def testNextSongWhenCurrentIsLast(self):
        self.getCurrentSong=self.playlist_1[14]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextSongCommand(playlistManager)
        self.assertRaises(PlaylistManagerException, command.execute)
    
    def testPreviousSongWhenCurrentIsNotFirst(self):
        self.getCurrentSong=self.playlist_1[8]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(7));
    
    def testPreviousSongWhenCurrentIsFirst(self):
        self.getCurrentSong=self.playlist_1[0]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousSongCommand(playlistManager)        
        self.assertRaises(PlaylistManagerException, command.execute)
        
    def testNextAlbumWhenCurrentIsNotLast(self):
        self.getCurrentSong=self.playlist_1[6]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(9));

    def testNextAlbumWhenCurrentIsLast_1(self):
        self.getCurrentSong=self.playlist_1[14]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)        
        self.assertRaises(PlaylistManagerException, command.execute)
      
    def testNextAlbumWhenCurrentIsLast_2_1(self):
        self.getCurrentSong=self.playlist_2[9]
        client = MockClient(self.getCurrentSong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(12));
  
    def testNextAlbumWhenCurrentIsLast_2_2(self):
        self.getCurrentSong=self.playlist_2[13]
        client = MockClient(self.getCurrentSong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayNextAlbumCommand(playlistManager)        
        self.assertRaises(PlaylistManagerException, command.execute)
                
    def testPreviousAlbumWhenCurrentIsNotFirst_1(self):
        self.getCurrentSong=self.playlist_1[8]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(3));
        
    def testPreviousAlbumWhenCurrentIsNotFirst_2(self):
        self.getCurrentSong=self.playlist_2[13]
        client = MockClient(self.getCurrentSong, self.playlist_2)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)
        command.execute()        
        self.assertEqual(client.getCurrentSong()['pos'], str(9));
        
    def testPreviousAlbumWhenCurrentIsFirst(self):
        self.getCurrentSong=self.playlist_1[2]
        client = MockClient(self.getCurrentSong, self.playlist_1)
        playlistManager = PlaylistManager(client);
        command = PlayPreviousAlbumCommand(playlistManager)        
        self.assertRaises(PlaylistManagerException, command.execute);
