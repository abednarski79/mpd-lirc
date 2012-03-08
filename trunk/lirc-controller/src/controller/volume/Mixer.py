'''
Created on 6 Mar 2012

@author: abednarski
'''

#import alsaaudio

class Mixer():
    
    def __init__(self, name = "Master", idx=0):
        #self.mixer = alsaaudio.Mixer(name, cardindex=idx)
        print "a"
        
    def setVolume(self, volume):        
        #self.mixer.setvolume(volume)
        print "a"
        
    def getVolume(self):
        #return self.mixer.getvolume()
        print "a"
        
    def mute(self):
        #self.mixer.setmute(1)
        print "a"
        
    def unMute(self):
        #self.mixer.setmute(0)
        print "a"
        
    def getMute(self):
        #self.mixer.getmute()
        print "a"        