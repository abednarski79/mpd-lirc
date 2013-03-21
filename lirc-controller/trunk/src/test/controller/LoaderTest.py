'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.loader import Loader
import unittest
import sys
import os

class LoaderTest(unittest.TestCase):
    
    def setUp(self):
        self.loader = Loader()
    
    def testLoadMyClass(self):
        method = self.loader.findMethodInstanceByName("MyTestModule", "MyTestClass", "myTestMethod")
        self.assertNotEqual(None, method, "Method is not populated.")        
    
    def testLoadMyClass2(self):
        method = self.loader.findMethodInstanceByName("mytestpackage.MyTestModule2", "MyTestClass2", "myTestMethod2")
        self.assertNotEqual(None, method, "Method 2 is not populated.")   
        method()
        
    def testLoadVolumeControllerAction(self):
        # reversing last two paths        
        lastPathEntry = sys.path.pop()
        sys.path.append("../../main/controller/")
        sys.path.append(lastPathEntry)
        method = self.loader.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp")
        self.assertNotEqual(None, method, "Method should be initiated")        
        