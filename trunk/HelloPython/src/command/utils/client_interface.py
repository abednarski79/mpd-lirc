'''
Created on 11 Oct 2011

@author: abednarski
'''
class Client:
    """The Client Abstract class"""
    def __init__(self):
            pass
    # Playback Control Commands
    #=========================
    #
    #goToNextSong                                           -> None
    #pause            <bool>                        -> None
    #playSongAtPosition             [<int>]                       -> None
    #playid           [<int>]                       -> None
    #goToPreviousSong                                       -> None
    #seek             <int>           <int>         -> None
    #seekid           <int>           <int>         -> None
    #stop                                           -> None
    def reset(self):
        pass
    def goToNextSong(self):
        pass
    def goToPreviousSong(self):
        pass
    def getCurrentSong(self):
        pass
    def findSongAtPosition(self, position):
        pass
    def playSongAtPosition(self, position):
        pass