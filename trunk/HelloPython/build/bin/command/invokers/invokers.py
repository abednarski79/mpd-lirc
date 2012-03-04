'''
Created on 11 Oct 2011

@author: abednarski
'''

class Invoker:
    
    def setCommand(self, command):
        pass
    
    def executeCommand(self):
        pass

class LoggingInvoker(Invoker):
    
    def setCommand(self, command):
        print "Command set to execute: ", command.__doc__
        self.command = command
        
    def executeCommand(self):
        print "Excuting command: ", self.command.__doc__
        return self.command.execute()