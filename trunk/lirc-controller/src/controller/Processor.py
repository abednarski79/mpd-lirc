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
        self.configuration = configuration
        self.executionQueue = []
        
    def preProcess(self, command, repeat):
        commandToExecute = self.configuration.buttons[command]
        self.executionQueue.append(commandToExecute)
        