'''
Created on 8 Oct 2011

@author: abednarski
'''
from mpd import CommandError

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PlaylistManagerException(Error):
    def __init__(self, msg):        
        self.msg = msg

class PlaylistManager():
    ''' This class is Receiver of playlist related commands in Command Pattern '''
    ''' Responsible for low level interaction with mpd client '''
    
    def __init__(self, client):
        print "Playlist manager: Initializing playlist manager"
        self.client = client
        
    def playNextSong(self):
        ''' get current song position 
            get from playlist song with position current+1
            if next song exist on the playlist move and return EX_OK
            if next position doesn't exist on the playlist return EX_FAIL '''
        print "Playlist manager: Entering playSongAtPosition next song method..."  
        try:      
            currentSong = self.client.getCurrentSong()
            currentSongPosition = int(currentSong['pos'])
            nextSongPosition = currentSongPosition + 1
            nextSong = self.client.findSongAtPosition(nextSongPosition)
            if nextSong is None:
                raise PlaylistManagerException("There is no next song in the playlist at position: ", nextSongPosition)            
            print "Playlist manager: Playing next song at position ", nextSongPosition
            self.client.playSongAtPosition(nextSongPosition)
        except CommandError as detail:
            raise PlaylistManagerException(detail)
        
    def playPreviousSong(self):
        ''' get current song position 
            get from playlist song with position current-1
            if previous song exist on the playlist move and return EX_OK
            if previous position doesn't exist on the playlist return EX_FAIL '''
        print "Playlist manager: Entering playSongAtPosition previous song method..."
        try:  
            currentSong = self.client.getCurrentSong()
            currentSongPosition = int(currentSong['pos'])
            previousSongPosition = currentSongPosition - 1
            previousSong = self.client.findSongAtPosition(previousSongPosition)
            if previousSong is None:
                raise PlaylistManagerException("There is no previous song in the playlist at position: ", previousSongPosition)            
            print "Playlist manager: Playing previous song at position ", previousSongPosition
            self.client.playSongAtPosition(previousSongPosition)
        except CommandError as detail:
            raise PlaylistManagerException(detail)
        
    def playNextAlbum(self):
        ''' get current song position and current song path
        loop over songs from the playlist and find one which directory differs from the current one
        for example current=song1=/playlist1/album1/song1.mp3 ... song12=/playlist1/album1/song12.mp3 ... song13=/playlist1/album2/song1.mp3
        will result in selecting song13'''
        print "Playlist manager: Entering playSongAtPosition next album method..."
        try:
            print "Playlist manager: retrieving current song"
            currentSong = self.client.getCurrentSong()
            if not currentSong:
                raise PlaylistManagerException("No current song")
            print "Playlist manager: retrieving current song position"
            currentSongPosition = int(currentSong['pos'])
            print "Playlist manager: current song position = ", currentSongPosition
            print "Playlist manager: retrieving current song file"
            currentSongFilePath = currentSong['file']
            print "Playlist manager: current song file = ", currentSongFilePath
            print "Playlist manager: calculating next song postition"
            nextSongPosition = currentSongPosition + 1
            print "Playlist manager: next song position = ", nextSongPosition
            nextSongFilePath = ''
            nextSong = ''
            # loop over songs in the playlist until find one with other path or end of playlist
            while (self.client.findSongAtPosition(nextSongPosition) is not None):            
                print "Playlist manager: Searching for next song at position: ", nextSongPosition 
                nextSong = self.client.findSongAtPosition(nextSongPosition)                
                nextSongFilePath = nextSong['file']                
                # if next song is in different directory then playSongAtPosition it and exit
                if not self.__albumEquals(currentSongFilePath, nextSongFilePath):
                    self.client.playSongAtPosition(nextSongPosition)
                    firstAlbumSong = nextSong 
                    print "Playlist manager: Playing next album starting from song: ", firstAlbumSong
                    return            
                nextSongPosition = nextSongPosition + 1            
            raise PlaylistManagerException("There is no next album in the playlist")
        except CommandError as detail:
            raise PlaylistManagerException(detail)
        
    def playPreviousAlbum(self):
        ''' get current song position and current song path
        loop in reverse over songs from the playlist and find one which directory differs from the current one
        for example: song1=/playlist1/album1/song1.mp3 ... song12=/playlist1/album1/song12.mp3 ... song13=/playlist1/album2/song1.mp3
        and current=song13
        will result in selecting song1 (and not song12 because it is last song in previous album)'''
        print "Playlist manager: Entering playSongAtPosition previous album method..."
        try:
            currentSong = self.client.getCurrentSong()
            if not currentSong:
                raise PlaylistManagerException("No current song")
            currentSongPosition = int(currentSong['pos'])
            currentSongFilePath = currentSong['file']
            previousSongPosition = currentSongPosition -1
            previousSongFilePath = ''
            previousSong = ''        
            # loop reverse over songs in the playlist until find one with other path or end of playlist
            while (self.client.findSongAtPosition(previousSongPosition) is not None):  
                print "Playlist manager: Searching for previous song at position: ", previousSongPosition           
                previousSong = self.client.findSongAtPosition(previousSongPosition)            
                previousSongFilePath = previousSong['file']
                # if previous song is in different directory then last song then previous album was found - step 1 of 2 done
                if not self.__albumEquals(currentSongFilePath, previousSongFilePath):
                    currentSong = previousSong;
                    currentSongPosition = previousSongPosition
                    currentSongFilePath = currentSong['file']
                    previousSongPosition = currentSongPosition -1
                    while (self.client.findSongAtPosition(previousSongPosition) is not None):
                        previousSong = self.client.findSongAtPosition(previousSongPosition)            
                        previousSongFilePath = previousSong['file']
                        if not self.__albumEquals(currentSongFilePath, previousSongFilePath):
                            self.client.playSongAtPosition(previousSongPosition + 1)  
                            firstAlbumSong = self.client.findSongAtPosition(previousSongPosition + 1)            
                            print "Playlist manager: Playing previous album starting from song: ", firstAlbumSong
                            return    
                        previousSongPosition = previousSongPosition - 1
                previousSongPosition = previousSongPosition - 1        
            raise PlaylistManagerException("There is no previous album in the playlist")
        except CommandError as detail:
            raise PlaylistManagerException(detail)
        
        
    def __albumEquals(self, song1FilePath, song2FilePath):
        print "Playlist manager: Comparing song path 1: ", song1FilePath, " with song path 2: ", song2FilePath
        if song1FilePath is None and song2FilePath is None:
            return True
        if song1FilePath is None and song2FilePath is not None:
            return False
        if song2FilePath is None and song1FilePath is not None:
            return False        
        song1Array = song1FilePath.split("/")
        print "Playlist manager: Song 1 file full path array: ", song1Array
        song2Array = song2FilePath.split("/")
        print "Playlist manager: Song 2 file full path array: ", song2Array
        # remove file name from path
        del song1Array[len(song1Array) - 1]
        print "Playlist manager: Song 1 file root path array: ", song1Array
        del song2Array[len(song2Array) - 1]
        print "Playlist manager: Song 2 file root path array: ", song2Array
        if song1Array == song2Array:
            print "Playlist manager: Song 1 and 2 root path match."
            return True
        print "Playlist manager: Song 1 and 2 root path are different"
        return False
    