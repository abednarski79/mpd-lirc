'''
Created on 10 Mar 2013

@author: abednarski
'''
from main.controller.Configuration import Configuration, Button, Action
import xml.etree.ElementTree as ET

class ConfigurationRead:
    
    def __init__(self, configurationPath):
        self.configurationPath = configurationPath
        
    def readConfiguration(self):    
        tree = ET.parse(self.configurationPath)
        root = tree.getroot()
        propertyElements = root.findall('properties/property')
        gapDuration = 0
        blocking = 0
        buttons = {}
        for propertyElement in propertyElements:
            propertyId = propertyElement.get("id")
            propertyValue = propertyElement.text
            if(propertyId == "gapDuration"):
                gapDuration = propertyValue
            elif(propertyId == "blocking"):
                blocking = propertyValue
        buttonElements = root.findall('buttons/button')
        for buttonElement in buttonElements:
            buttonId = buttonElement.get("id")
            button = Button(buttonId)
            actionElements = buttonElement.findall('action')
            for actionElement in actionElements:
                actionId = actionElement.get("id")
                actionType = actionElement.get("type")
                fireDelay = 0
                isCancelable = True
                minimalRepeatTrigger = 0
                taskElement = actionElement.find("task")
                module = taskElement.find("module").text
                clazz = taskElement.find("class").text
                method = taskElement.find("method").text
                task = module + "." + clazz + "." + method + "()#"        
                isCancelableElement = actionElement.find("isCancelable")
                if(isCancelableElement != None):
                    isCancelable = isCancelableElement.text        
                fireDelayElement = actionElement.find("fireDelay")
                if(fireDelayElement != None):
                    fireDelay = fireDelayElement.text
                action = Action(actionId, task, fireDelay, isCancelable, minimalRepeatTrigger)            
                if (actionType == "CLICK"):
                    button.click = action
                elif (actionType == "DOUBLE_CLICK"):
                    button.doubleClick = action
                else:
                    button.hold = action        
            buttons[button.id]=button  
        return Configuration(gapDuration, blocking, buttons)
