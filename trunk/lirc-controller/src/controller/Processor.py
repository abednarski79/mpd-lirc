'''
Created on 11 Mar 2012

@author: abednarski
'''

class Processor():
    '''
    classdocs
    '''
    executionQueue = []
    
    def __init__(self, configuration):
        self.configurationMap = {}
        for button in configuration.buttons:
            self.configurationMap[button.key] = button
        self.executionQueue = []
        
    def preProcess(self, button, repeat):
        commandToExecute = self.configurationMap[button.key]
        self.executionQueue.append(commandToExecute.click.action)
        