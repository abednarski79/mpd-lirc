'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.loader import Loader
import unittest
import sys

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
        sys.path.append("/home/abednarski/workspace3/lirc-controller_trunk/src/main/controller")
        method = self.loader.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp")
        self.assertNotEqual(None, method, "Method should be initiated")        
        