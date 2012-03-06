'''
Created on 6 Mar 2012

@author: abednarski
'''

import alsaaudio

class Mixer():
    
    def __init__(self, name = "Master", idx=0):
        self.mixer = alsaaudio.Mixer(name, cardindex=idx)
    
    def setVolume(self, volume):        
        self.mixer.setvolume(volume)
        
    def getVolume(self, volume):
        return self.mixer.getvolume()
    
    def mute(self):
        self.mixer.setmute(1)
    
    def unMute(self):
        self.mixer.setmute(0)
        
    def getMute(self):
        self.mixer.getmute()        