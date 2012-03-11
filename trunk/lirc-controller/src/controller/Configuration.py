'''
Created on 11 Mar 2012

@author: abednarski
'''

class Button():
    
    def __init__(self, command, firstClick, doubleClick, longClick):
        self.command = command
        self.firstClick = firstClick
        self.doubleClick = doubleClick
        self.longClick = longClick
        
    
class Configuration():
    '''
    classdocs
    '''
    gapDuration = None;
    
    def __init__(self, buttons= None, configurationPath = None):
        if configurationPath == None:
            self.buttons = buttons
        else:
            self.buttons = self.loadConfiguration(configurationPath)            
    
    def loadConfiguration(self):
        pass
    