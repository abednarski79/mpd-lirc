'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.loader import Loader
import unittest
import sys

class LoaderTest(unittest.TestCase):
    
    def setUp(self):
        self.classLoader = Loader()
        # swap last two paths to change the class search order    
        lastPathEntry = sys.path.pop()
        sys.path.append("../../main/controller/")
        sys.path.append(lastPathEntry)
    
    def testLoadMyClass(self):
        method = self.classLoader.findMethodInstanceByName("MyTestModule", "MyTestClass", "myTestMethod")
        self.assertNotEqual(None, method, "Method is not populated.")        
    
    def testLoadMyClass2(self):
        method = self.classLoader.findMethodInstanceByName("mytestpackage.MyTestModule2", "MyTestClass2", "myTestMethod2")
        self.assertNotEqual(None, method, "Method 2 is not populated.")   
        method()
        
    def testLoadVolumeControllerAction(self):
        method = self.classLoader.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp")
        self.assertNotEqual(None, method, "Method should be initiated")                

    def testLoadShellControllerAction(self):        
        method = self.classLoader.findMethodInstanceByName("shell.ShellController", "ShellController", "executeCommand")
        self.assertNotEqual(None, method, "Method should be initiated")          