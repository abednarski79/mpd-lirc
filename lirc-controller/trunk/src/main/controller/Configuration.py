'''
Created on 11 Mar 2012

@author: abednarski
'''

class Action():    
    def __init__(self, id, task, fireDelay = 0, isCancelable = True, minimalRepeatTrigger = 0):
        self.id = id
        self.task = task
        self.fireDelay = fireDelay
        self.isCancelable = isCancelable
        self.minimalRepeatTrigger = minimalRepeatTrigger
    def __str__(self):
        return "Action: id = %s, task = %s" % (self.id, self.task)
        
class Button():    
    def __init__(self, id, click = None, doubleClick = None, hold = None):
        self.id = id
        self.click = click
        self.doubleClick = doubleClick
        self.hold = hold
    def __str__(self):
        return "Button: id = %s, click = %s, double click = %s, hold = %s" % (self.id, self.click.id, self.doubleClick.id, self.hold.id)           
    
class Configuration():    
    def __init__(self, gapDuration, blocking, buttons):
        self.gapDuration = gapDuration
        self.blocking = blocking
        self.buttons = buttons
    def __str__(self):
        return "Configuration: gap duration = %s, blocking = %s, buttons = %s" % (self.gapDuration, self.blocking, self.buttons)              