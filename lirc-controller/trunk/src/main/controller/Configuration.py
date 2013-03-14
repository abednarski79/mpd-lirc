'''
Created on 11 Mar 2012

@author: abednarski
'''
import xml.etree.ElementTree as ET

class Action():    
    def __init__(self, id, task, fireDelay = 0, isCancelable = True, minimalRepeatTrigger = 0):
        self.id = id
        self.task = task
        self.fireDelay = fireDelay
        self.isCancelable = isCancelable
        self.minimalRepeatTrigger = minimalRepeatTrigger
    def __str__(self):
        return "Action: id = %s, task = %s" % (self.id, self.task)
        
class Button():    
    def __init__(self, id, click = None, doubleClick = None, hold = None):
        self.id = id
        self.click = click
        self.doubleClick = doubleClick
        self.hold = hold
    def __str__(self):
        return "Button: id = %s, click = %s, double click = %s, hold = %s" % (self.id, self.click.id, self.doubleClick.id, self.hold.id)           
    
class Configuration():    
    def __init__(self, gapDuration, blocking, buttons):
        self.gapDuration = gapDuration
        self.blocking = blocking
        self.buttons = buttons
    def __str__(self):
        return "Configuration: gap duration = %s, blocking = %s, buttons = %s" % (self.gapDuration, self.blocking, self.buttons)

class ConfigurationRead:
    
    def __init__(self, configurationPath):
        self.configurationPath = configurationPath
        
    def readConfiguration(self):   
        gapDuration = 0
        blocking = 0
        buttons = {}
        tree = ET.parse(self.configurationPath) # tree = ET.parse('../../../resources/configuration.xml')
        root = tree.getroot()
        propertyElements = root.findall('properties/property')
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