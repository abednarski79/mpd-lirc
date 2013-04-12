'''
Created on 21 Mar 2013

@author: abednarski
'''
import subprocess

class ShellController():
    def executeCommand(self, command):
        subprocess.call(command, shell=True)