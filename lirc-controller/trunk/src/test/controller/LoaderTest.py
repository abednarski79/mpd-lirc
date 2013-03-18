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
    
    def testLoadVolumeControllerAction(self):
        sys.path.append("/home/abednarski/workspace3/lirc-controller_trunk/src/main/controller")
        method = self.loader.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp")
        self.assertNotEqual(None, method, "Method should be initiated")
        