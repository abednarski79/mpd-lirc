'''
Created on 11 Mar 2012

@author: abednarski
'''
from controller.Configuration import Configuration, Button
from controller.Processor import Processor
import time
import unittest

gapDuration = 2

class ProcessorTest(unittest.TestCase):
    
    def setUp(self):
        print "Setup processor"
        configuration = Configuration(None)
        plusButton = Button("PLUS-BUTTON", "plus-action")
        minutButton = Button("MINUS-BUTTON", "minus-action")
        plusButton = Button("PLUS-BUTTON", "plus-action")
        minutButton = Button("MINUS-BUTTON", "minus-action")
        
        button_A = Button("A_button", "A_singleClick", "A_doubleClick", "A_longClick")
        buttons = {button_A.command: button_A}
        configuration.buttons = buttons
        global gapDuration
        configuration.gapDuration = gapDuration
        self.processor = Processor(configuration)

    def tearDown(self):
        self.processor= None
                

    def createCommand(self, command, repeat):
        global gapDuration
        self.processor.preProcess(command, repeat)
        time.sleep(gapDuration)
        
    def testPlusButton(self):
        # button that immediately reacts on button event
        self.createCommand("A_button", 0)        
        self.createCommand("A_button", 0)
        self.assertEqual(len(self.processor.executionQueue), 2, "Expected number of command should be 2 but is: %s" %(len(self.processor.executionQueue)));
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1ClickCommand']
    unittest.main()