'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.Configuration import Configuration, ConfigurationRead, Button, Action
from main.controller.volume.VolumeController import VolumeController
import unittest


class ProcessorTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test1(self):
        configurationReader = ConfigurationRead("../../../resources/test/configuration-test1.xml")
        expectedGapDuration = 10
        expectedBlocking = 20
        expectedButtons = {}
        task = VolumeController().volumeUp
        expectedActionClick = Action("VOLUME_UP", task, isCancelable = False)
        expectedActionDoubleClick = Action("VOLUME_UP", task, isCancelable = False)
        expectedActionHold = Action("VOLUME_UP", task, isCancelable = False)
        expectedButtons["PLUS_ID"] = Button("PLUS_ID", click = expectedActionClick, doubleClick = expectedActionDoubleClick, hold = expectedActionHold)
        actualConfiguration = configurationReader.readConfiguration()
        expecteConfiguration = Configuration(expectedGapDuration, expectedBlocking, expectedButtons)
        self.assertEqual(len(expecteConfiguration.buttons), len(actualConfiguration.buttons), "Number of buttons is incorrect")
        actualButton = actualConfiguration.buttons["PLUS_ID"]
        self.assertNotEqual(actualButton, None, "Expected button not present")
        actualClickAction = actualButton.click
        self.assertNotEqual(None, actualClickAction, "Click action is not populated")
        self.assertEqual(expectedActionClick, actualClickAction, "Click action parameters should match")
        actualDoubleClickAction = actualButton.doubleClick
        self.assertNotEqual(None, actualDoubleClickAction, "Double click action is not populated")
        actualHoldButton = actualButton.hold
        self.assertNotEqual(None, actualHoldButton, "Hold action is not populated")
        
        
        # self.assertEqual(len(actuallConfiguration.buttons), len(expecteConfiguration.buttons), "Number of buttons is incorrect")
    
    """def test2(self):
        configurationReader = ConfigurationRead("/resources/test/configuration-test2.xml")"""
    