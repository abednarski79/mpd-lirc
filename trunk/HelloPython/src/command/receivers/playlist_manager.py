'''
Created on 8 Oct 2011

@author: abednarski
'''
import command.utils.constants as constants

class PlaylistManager():
    ''' This class is Receiver of playlist related commands in Command Pattern '''
    ''' Responsible for low level interaction with mpd client '''
    
    def __init__(self, client):
        print "Initializing playlist manager"
        self.client = client
        
    def playNextSong(self):
        ''' get current song position 
            get from playlist song with position current+1
            if next song exist on the playlist move and return EX_OK
            if next position doesn't exist on the playlist return EX_FAIL '''
        print "Entering play next song method..."        
        currentSong = self.client.currentsong()
        currentSongPosition = int(currentSong['pos'])
        nextSongPosition = currentSongPosition + 1
        nextSong = self.client.playlistid(nextSongPosition)
        if nextSong is None:
            print "There is no next song in the playlist at position: ", nextSongPosition
            return constants.EX_FAIL
        print "Playing next song at position ", nextSongPosition
        self.client.play(nextSongPosition)
        return constants.EX_OK        
        
    def playPreviousSong(self):
        ''' get current song position 
            get from playlist song with position current-1
            if previous song exist on the playlist move and return EX_OK
            if previous position doesn't exist on the playlist return EX_FAIL '''
        print "Entering play previous song method..."        
        currentSong = self.client.currentsong()
        currentSongPosition = int(currentSong['pos'])
        previousSongPosition = currentSongPosition - 1
        previousSong = self.client.playlistid(previousSongPosition)
        if previousSong is None:
            print "There is no previous song in the playlist at position: ", previousSongPosition
            return constants.EX_FAIL
        print "Playing previous song at position ", previousSongPosition
        self.client.play(previousSongPosition)
        return constants.EX_OK
        
    def playNextAlbum(self):
        ''' get current song position and current song path
        loop over songs from the playlist and find one which directory differs from the current one
        for example current=song1=/playlist1/album1/song1.mp3 ... song12=/playlist1/album1/song12.mp3 ... song13=/playlist1/album2/song1.mp3
        will result in selecting song13'''
        print "Entering play next album method..."
        currentSong = self.client.currentsong()
        currentSongPosition = int(currentSong['pos'])
        currentSongFilePath = currentSong['file']
        nextSongPosition = currentSongPosition + 1
        nextSongFilePath = ''
        nextSong = ''
        # loop over songs in the playlist until find one with other path or end of playlist
        while (self.client.playlistid(nextSongPosition) is not None):            
            nextSong = self.client.playlistid(nextSongPosition)            
            nextSongFilePath = nextSong['file']
            # if next song is in different directory then play it and exit
            if not self.__albumEquals(currentSongFilePath, nextSongFilePath):
                self.client.play(nextSongPosition)
                print "Playing next album at song position ", nextSongPosition
                return constants.EX_OK            
            nextSongPosition = nextSongPosition + 1            
        print "There is no next album in the playlist"
        return constants.EX_FAIL
        
    def playPreviousAlbum(self):
        ''' get current song position and current song path
        loop in reverse over songs from the playlist and find one which directory differs from the current one
        for example: song1=/playlist1/album1/song1.mp3 ... song12=/playlist1/album1/song12.mp3 ... song13=/playlist1/album2/song1.mp3
        and current=song13
        will result in selecting song1 (and not song12 because it is last song in previous album)'''
        print "Entering play previous album method..."
        currentSong = self.client.currentsong()
        currentSongPosition = int(currentSong['pos'])
        currentSongFilePath = currentSong['file']
        previousSongPosition = currentSongPosition -1
        previousSongFilePath = ''
        previousSong = ''        
        # loop reverse over songs in the playlist until find one with other path or end of playlist
        while (self.client.playlistid(previousSongPosition) is not None):            
            previousSong = self.client.playlistid(previousSongPosition)            
            previousSongFilePath = previousSong['file']
            # if previous song is in different directory then last song then previous album was found - step 1 of 2 done
            if not self.__albumEquals(currentSongFilePath, previousSongFilePath):
                currentSong = previousSong;
                currentSongPosition = previousSongPosition
                currentSongFilePath = currentSong['file']
                previousSongPosition = currentSongPosition -1
                while (self.client.playlistid(previousSongPosition) is not None):
                    previousSong = self.client.playlistid(previousSongPosition)            
                    previousSongFilePath = previousSong['file']
                    if not self.__albumEquals(currentSongFilePath, previousSongFilePath):
                        self.client.play(previousSongPosition + 1)
                        print "Playing previous album at song position ", (previousSongPosition + 1)
                        return constants.EX_OK    
                    previousSongPosition = previousSongPosition - 1
            previousSongPosition = previousSongPosition - 1        
        print "There is no previous album in the playlist"
        return constants.EX_FAIL
        
        
    def __albumEquals(self, song1FilePath, song2FilePath):
        print "Comparing song path 1: ", song1FilePath, " with song path 2: ", song2FilePath
        if song1FilePath is None and song2FilePath is None:
            return True
        if song1FilePath is None and song2FilePath is not None:
            return False
        if song2FilePath is None and song1FilePath is not None:
            return False        
        song1Array = song1FilePath.split("/")
        print "Song 1 file full path array: ", song1Array
        song2Array = song2FilePath.split("/")
        print "Song 2 file full path array: ", song2Array
        # remove file name from path
        del song1Array[len(song1Array) - 1]
        print "Song 1 file root path array: ", song1Array
        del song2Array[len(song2Array) - 1]
        print "Song 2 file root path array: ", song2Array
        if song1Array == song2Array:
            print "Song 1 and 2 root path match."
            return True
        print "Song 1 and 2 root path are different"
        return False
    