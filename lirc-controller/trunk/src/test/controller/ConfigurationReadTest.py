'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.Configuration import Configuration, ConfigurationRead, \
    Button, Action
from main.controller.loader import Loader
from main.controller.mpd.MpdController import MpdController
from main.controller.volume.VolumeController import VolumeController
import mox
import unittest

class ConfigurationReaderTest(unittest.TestCase):
    
    def setUp(self):
        self.mocker = mox.Mox()
        self.classLoaderMock = self.mocker.CreateMock(Loader)
    
    def testFile1(self):
        # setup
        configurationReader = ConfigurationRead("../../../resources/test/configuration-test1.xml", self.classLoaderMock)
        expectedGapDuration = 10
        expectedBlocking = 20
        expectedButtons = {}
        task = VolumeController().volumeUp
        expectedActionClick = Action("VOLUME_UP", task, isCancelable = False)
        expectedActionDoubleClick = Action("VOLUME_UP", task, isCancelable = False)
        expectedActionHold = Action("VOLUME_UP", task, isCancelable = False)
        expectedButtons["PLUS_ID"] = Button("PLUS_ID", click = expectedActionClick, doubleClick = expectedActionDoubleClick, hold = expectedActionHold)
        expecteConfiguration = Configuration(expectedGapDuration, expectedBlocking, expectedButtons)
        # record mock sequence
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task)
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task)
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task)
        # replay mock sequence
        self.mocker.ReplayAll()
        # test
        actualConfiguration = configurationReader.readConfiguration()
        # check    
        self.mocker.VerifyAll()
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
        
        
    def testFile2(self):
        # setup
        configurationReader = ConfigurationRead("../../../resources/test/configuration-test2.xml", self.classLoaderMock)
        expectedGapDuration = 6
        expectedBlocking = 5
        expectedButtons = {}
        expectedNextAlbumTask = MpdController().nextAlbum
        expectedNextSongTask = MpdController().nextSong
        expectedSkipForwardTask = MpdController().skipForward
        expectedActionClick = Action("NEXT_SONG", expectedNextSongTask, fireDelay = 0.22)
        expectedActionDoubleClick = Action("NEXT_ALBUM", expectedNextAlbumTask, fireDelay = 0.22)
        expectedActionHold = Action("SKIP_FORWARD", expectedSkipForwardTask, minimalRepeatTrigger = 1)
        expectedButtons["FORWARD_ID"] = Button("FORWARD_ID", click = expectedActionClick, doubleClick = expectedActionDoubleClick, hold = expectedActionHold)
        expecteConfiguration = Configuration(expectedGapDuration, expectedBlocking, expectedButtons)
        # record mock sequence
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "nextSong").AndReturn(expectedNextSongTask)
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "nextAlbum").AndReturn(expectedNextAlbumTask)
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "skipForward").AndReturn(expectedSkipForwardTask)
        # replay mock sequence
        self.mocker.ReplayAll()
        # test
        actualConfiguration = configurationReader.readConfiguration()
        # check    
        self.mocker.VerifyAll()
        self.assertEqual(len(expecteConfiguration.buttons), len(actualConfiguration.buttons), "Number of buttons is incorrect")
        actualButton = actualConfiguration.buttons["FORWARD_ID"]
        self.assertNotEqual(actualButton, None, "Expected button not present")
        actualClickAction = actualButton.click
        self.assertNotEqual(None, actualClickAction, "Click action is not populated")
        self.assertEqual(expectedActionClick, actualClickAction, "Click action parameters should match")
        actualDoubleClickAction = actualButton.doubleClick
        self.assertNotEqual(None, actualDoubleClickAction, "Double click action is not populated")
        actualHoldButton = actualButton.hold
        self.assertNotEqual(None, actualHoldButton, "Hold action is not populated")