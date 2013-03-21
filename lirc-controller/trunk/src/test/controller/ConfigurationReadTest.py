'''
Created on 18 Mar 2013

@author: abednarski
'''
from main.controller.Configuration import Configuration, ConfigurationRead, \
    Button, Action
from main.controller.loader import Loader
from main.controller.mpd.MpdController import MpdController
from main.controller.volume.VolumeController import VolumeController
from main.controller.shell.ShellController import ShellController
import mox
import unittest

class ConfigurationReaderTest(unittest.TestCase):
    
    def setUp(self):
        self.mocker = mox.Mox()
        self.classLoaderMock = self.mocker.CreateMock(Loader)
    
    def testFile1SingleButton(self):
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
        
        
    def testFile2SingleButton(self):
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

    def testFile3TwoButtons(self):
        # setup
        configurationReader = ConfigurationRead("../../../resources/test/configuration-test3.xml", self.classLoaderMock)
        expectedGapDuration = 6
        expectedBlocking = 5
        expectedButtons = {}
        task1 = VolumeController().volumeUp
        expectedActionClick1 = Action("VOLUME_UP", task1, isCancelable = False)
        expectedActionDoubleClick1 = Action("VOLUME_UP", task1, isCancelable = False)
        expectedActionHold1 = Action("VOLUME_UP", task1, isCancelable = False)
        expectedButtons["PLUS_ID"] = Button("PLUS_ID", click = expectedActionClick1, doubleClick = expectedActionDoubleClick1, hold = expectedActionHold1)        
        expectedNextAlbumTask2 = MpdController().nextAlbum
        expectedNextSongTask2 = MpdController().nextSong
        expectedSkipForwardTask2 = MpdController().skipForward
        expectedActionClick2 = Action("NEXT_SONG", expectedNextSongTask2, fireDelay = 0.22)
        expectedActionDoubleClick2 = Action("NEXT_ALBUM", expectedNextAlbumTask2, fireDelay = 0.22)
        expectedActionHold2 = Action("SKIP_FORWARD", expectedSkipForwardTask2, minimalRepeatTrigger = 1)        
        expectedButtons["FORWARD_ID"] = Button("FORWARD_ID", click = expectedActionClick2, doubleClick = expectedActionDoubleClick2, hold = expectedActionHold2)
        expecteConfiguration = Configuration(expectedGapDuration, expectedBlocking, expectedButtons)
        # record mock sequence
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task1)
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task1)
        self.classLoaderMock.findMethodInstanceByName("volume.VolumeController", "VolumeController", "volumeUp").AndReturn(task1)        
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "nextSong").AndReturn(expectedNextSongTask2)
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "nextAlbum").AndReturn(expectedNextAlbumTask2)
        self.classLoaderMock.findMethodInstanceByName("mpd.MpdController", "MpdController", "skipForward").AndReturn(expectedSkipForwardTask2)
        # replay mock sequence
        self.mocker.ReplayAll()
        # test
        actualConfiguration = configurationReader.readConfiguration()
        # check    
        self.mocker.VerifyAll()
        self.assertEqual(len(expecteConfiguration.buttons), len(actualConfiguration.buttons), "Number of buttons is incorrect")
        actualButton1 = actualConfiguration.buttons["PLUS_ID"]
        self.assertNotEqual(actualButton1, None, "Expected button 1 not present")
        actualClickAction1 = actualButton1.click
        self.assertNotEqual(None, actualClickAction1, "Click action 1 is not populated")
        self.assertEqual(expectedActionClick1, actualClickAction1, "Click action 1 parameters should match")
        actualDoubleClickAction1 = actualButton1.doubleClick
        self.assertNotEqual(None, actualDoubleClickAction1, "Double click action is not populated")
        actualHoldButton1 = actualButton1.hold
        self.assertNotEqual(None, actualHoldButton1, "Hold action 1 is not populated")        
        actualButton2 = actualConfiguration.buttons["FORWARD_ID"]
        self.assertNotEqual(actualButton2, None, "Expected button not present")
        actualClickAction2 = actualButton2.click
        self.assertNotEqual(None, actualClickAction2, "Click action 2 is not populated")
        self.assertEqual(expectedActionClick2, actualClickAction2, "Click action 2 parameters should match")
        actualDoubleClickAction2 = actualButton2.doubleClick
        self.assertNotEqual(None, actualDoubleClickAction2, "Double click action 2 is not populated")
        actualHoldButton2 = actualButton2.hold
        self.assertNotEqual(None, actualHoldButton2, "Hold action 2 is not populated")
        
    def testFile4ParameterizedAction(self):
        # setup
        configurationReader = ConfigurationRead("../../../resources/test/configuration-test4.xml", self.classLoaderMock)
        expectedGapDuration = 10
        expectedBlocking = 20
        expectedButtons = {}
        task = ShellController().executeCommand
        expectedActionClick = Action("PLAY_PAUSE", task, parameter = "/some/path/to/shell/script/play_pause.sh", fireDelay = 0.22)
        expectedActionDoubleClick = Action("PLAY_PAUSE", task, parameter = "/some/path/to/shell/script/play_pause.sh", fireDelay = 0.22)
        expectedActionHold = Action("POWER_OFF", task, parameter = "/some/path/to/shell/script/power_off.sh", minimalRepeatTrigger = 5)
        expectedButtons["PLAY_ID"] = Button("PLAY_ID", click = expectedActionClick, doubleClick = expectedActionDoubleClick, hold = expectedActionHold)
        expecteConfiguration = Configuration(expectedGapDuration, expectedBlocking, expectedButtons)
        # record mock sequence
        self.classLoaderMock.findMethodInstanceByName("shell.ShellController", "ShellController", "executeCommand").AndReturn(task)
        self.classLoaderMock.findMethodInstanceByName("shell.ShellController", "ShellController", "executeCommand").AndReturn(task)
        self.classLoaderMock.findMethodInstanceByName("shell.ShellController", "ShellController", "executeCommand").AndReturn(task)
        # replay mock sequence
        self.mocker.ReplayAll()
        # test
        actualConfiguration = configurationReader.readConfiguration()
        # check    
        self.mocker.VerifyAll()
        self.assertEqual(len(expecteConfiguration.buttons), len(actualConfiguration.buttons), "Number of buttons is incorrect")
        actualButton = actualConfiguration.buttons["PLAY_ID"]
        self.assertNotEqual(actualButton, None, "Expected button not present")
        actualClickAction = actualButton.click
        self.assertNotEqual(None, actualClickAction, "Click action is not populated")
        self.assertEqual(expectedActionClick, actualClickAction, "Click action parameters should match")
        actualDoubleClickAction = actualButton.doubleClick
        self.assertNotEqual(None, actualDoubleClickAction, "Double click action is not populated")
        actualHoldButton = actualButton.hold
        self.assertNotEqual(None, actualHoldButton, "Hold action is not populated")     