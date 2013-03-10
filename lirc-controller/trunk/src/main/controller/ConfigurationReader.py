'''
Created on 10 Mar 2013

@author: abednarski
'''
import xml.etree.ElementTree as ET
tree = ET.parse('../../../resources/configuration.xml')
root = tree.getroot()
"""properties = root.findall('properties/property')
blocking = 0;
for property in properties:
    if(property.get("name") == "blocking"):
        blocking = property.text"""

buttonElements = root.findall('buttons/button')
for buttonElement in buttonElements:
    actionElements = buttonElement.findall('action')
    for actionElement in actionElements:
        name = actionElement.get("name")
        isCancelableElement = actionElement.find("isCancelable")
        if(isCancelableElement != None):
            print isCancelableElement.text        
        fireDelayElement = actionElement.find("fireDelay")
        if(fireDelayElement != None):
            print fireDelayElement.text
