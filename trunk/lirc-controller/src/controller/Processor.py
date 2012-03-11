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
        executionCommands = self.configuration[command]
        self.executionQueue.append(command)
        
        