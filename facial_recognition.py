#Author: Steven Broussard
#Date Created: January 14, 2017
#Project Name: Familiar Face
#File Name: facial_recognition.py

import os
# import ryan's 

pathOutputFile = "./output.txt"
inputInformationOfPhoto = ""

class readWrite(object):
    
    # initialize the class
    def __init__(self, object):
        self.object = object

    # Read file from java
    def readFileInput(self, pathInputFile):
        fileObject = open(pathInputFile, 'r')
        inputInformationOfPhoto = fileObject.read()
        fileObject.close()

        return inputInformationOfPhoto

    # facial recognition program from Ryan

    # write in file information from recog method
    def writeToFile(self, inputInformationOfPhoto):
        fileobject2 = open(pathOutputFile, 'w')
        fileobject2.write(inputInformationOfPhoto)
        fileobject2.close()
