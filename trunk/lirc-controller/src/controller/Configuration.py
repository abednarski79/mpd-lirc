'''
Created on 11 Mar 2012

@author: abednarski
'''

class Action():    
    def __init__(self, action, fireDelay = 0, isCancelable = True, minimalRepeatTrigger = 0):
        self.action = action
        self.fireDelay = fireDelay
        self.isCancelable = isCancelable
        self.minimalRepeatTrigger = minimalRepeatTrigger
        
class Button():    
    def __init__(self, key, click, doubleClick, hold):
        self.key = key
        self.click = click
        self.doubleClick = doubleClick
        self.hold = hold              
    
class Configuration():
    '''
    classdocs
    '''
    
    def __init__(self, gapDuration, buttons = None, configurationPath = None):
        self.gapDuration = gapDuration
        if configurationPath == None:
            self.buttons = buttons
        else:
            self.buttons = self.loadConfiguration(configurationPath)            
    
    def loadConfiguration(self):
        pass
    