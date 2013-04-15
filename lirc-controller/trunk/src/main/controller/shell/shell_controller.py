'''
Created on 21 Mar 2013

@author: abednarski
'''
import subprocess
import logging

class ShellController():
    
    def __init__(self):
        self.logger = logging.getLogger("controllerApp")
        
    def executeCommand(self, command):
        self.logger.debug("Running shell command: %s" % command)
        subprocess.call(command, shell=True)