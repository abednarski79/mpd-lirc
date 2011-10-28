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
    #next                                           -> None
    #pause            <bool>                        -> None
    #play             [<int>]                       -> None
    #playid           [<int>]                       -> None
    #previous                                       -> None
    #seek             <int>           <int>         -> None
    #seekid           <int>           <int>         -> None
    #stop                                           -> None
    def reset(self):
        pass
    def next(self):
        pass
    def previous(self):
        pass
    def currentsong(self):
        pass
    def playlistid(self, position):
        pass
    def play(self, position):
        pass