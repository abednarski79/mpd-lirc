'''
Created on 11 Mar 2012

@author: abednarski
'''

from main.controller.loader import Loader
import xml.etree.ElementTree as ET
import logging

class Task():    
    def __init__(self, module, clazz, method):
        self.module = module
        self.clazz = clazz
        self.method = method
    
class Action():    
    def __init__(self, id, task, parameter = None, fireDelay = 0, isCancelable = True, minimalRepeatTrigger = 0):
        self.id = id
        self.task = task
        self.fireDelay = fireDelay
        self.isCancelable = isCancelable
        self.minimalRepeatTrigger = minimalRepeatTrigger
        self.parameter = parameter
    
    def __str__(self):
        return "Action: id = %s" % (self.id)
    
    def __cmp__(self, otherAction):
        if(otherAction == None):
            return -1
        if(self.id != otherAction.id):
            return -1
        if(self.task != otherAction.task):
            return -1
        if(self.parameter != otherAction.parameter):
            return -1        
        if(self.fireDelay != otherAction.fireDelay):
            return -1
        if(self.isCancelable != otherAction.isCancelable):
            return -1
        if(self.minimalRepeatTrigger != otherAction.minimalRepeatTrigger):
            return -1    
        return 0


class Button():        
    def __init__(self, id, click = None, doubleClick = None, hold = None):
        self.id = id
        self.click = click
        self.doubleClick = doubleClick
        self.hold = hold
        print "self id %s" % (self.id)
    
    def __str__(self):
        return "Button: id = %s, click = %s, double click = %s, hold = %s" % (self.id, self.click, self.doubleClick, self.hold)        
    
    def __cmp__(self, otherButton):
        if(otherButton == None):
            return -1
        if(self.id != otherButton.id):
            return -1
        if(self.click != otherButton.click):
            return -1
        if(self.doubleClick != otherButton.doubleClick):
            return -1
        if(self.hold != otherButton.hold):
            return -1
        return 0
                   
    
class Configuration():    
    def __init__(self, gapDuration, blocking, buttons):
        self.gapDuration = gapDuration
        self.blocking = blocking
        self.buttons = buttons
    
    def __str__(self):
        return "Configuration: gap duration = %s, blocking = %s, buttons = %s" % (self.gapDuration, self.blocking, self.buttons)              

class ConfigurationReader:    
    def __init__(self, configurationPath, classLoader = None):
        self.logger = logging.getLogger("controllerApp")
        self.configurationPath = configurationPath
        if(classLoader == None):
            self.classLoader = Loader()
        else:
            self.classLoader = classLoader
        
    def readConfiguration(self):   
        gapDuration = 0
        blocking = 0
        buttons = {}
        self.logger.info("Reading configuration from %s" % self.configurationPath)        
        tree = ET.parse(self.configurationPath)
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
            self.logger.debug("Found new button with id: %s" % buttonId)
            button = Button(buttonId)
            actionElements = buttonElement.findall('action')
            for actionElement in actionElements:
                actionId = actionElement.get("id")
                actionType = actionElement.get("type")
                fireDelay = 0
                isCancelable = True
                minimalRepeatTrigger = 0
                parameter = None
                taskElement = actionElement.find("task")
                moduleName = taskElement.find("module").text
                className = taskElement.find("class").text
                methodName = taskElement.find("method").text                
                task = Task(moduleName, className, methodName)                 
                isCancelableElement = actionElement.find("isCancelable")
                if(isCancelableElement != None):
                    if(isCancelableElement.text.lower == "true"):
                        isCancelable = True
                    else:
                        isCancelable = False
                fireDelayElement = actionElement.find("fireDelay")
                if(fireDelayElement != None):
                    fireDelay = float(fireDelayElement.text)
                parameterElement = taskElement.find("parameter")
                if(parameterElement != None):
                    parameter = parameterElement.text
                minimalRepeatTriggerElement = actionElement.find("minimalRepeatTrigger")
                if(minimalRepeatTriggerElement != None):
                    minimalRepeatTrigger = int(minimalRepeatTriggerElement.text) 
                action = Action(actionId, task, parameter, fireDelay, isCancelable, minimalRepeatTrigger)            
                if (actionType == "CLICK"):
                    button.click = action
                elif (actionType == "DOUBLE_CLICK"):
                    button.doubleClick = action
                else:
                    button.hold = action
            buttons[button.id]=button
            self.logger.debug("Adding new button: %s" % button)        
        return Configuration(gapDuration, blocking, buttons)

class ClassCache():
    pass

class ClassCacheInitializator:
    def loadClasses(self):
        # task = self.classLoader.findMethodInstanceByName(moduleName, className, methodName)
        return ClassCache
