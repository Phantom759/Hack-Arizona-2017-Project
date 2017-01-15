#Author: Steven Broussard
#Date Created: January 14, 2017
#Project Name: Familiar Face
#File Name: facial_recognition.py

import os
from FacetoPerson import *

pathOutputFile = "./storage/emulated/0/DCIM/Camera/pythonToJava.txt"

class readWrite(object):
    
    # initialize the class
    def __init__(self, object):
        self.object = object

    # call the matching function
    def readFileInput(self, pathInputFile):
        #fileObject = open(pathInputFile, 'r')
        #inputInformationOfPhoto = fileObject.read()
        #fileObject.close()
        #return inputInformationOfPhoto

        # return variable from matching method
        name = matcher()
        return name

    # write in file information from recog method
    def writeToFile(self, inputInformationOfPhoto):
        fileobject2 = open(pathOutputFile, 'w')
        fileobject2.write(inputInformationOfPhoto)
        fileobject2.close()

# return the path of the photo
def photoPath():
    return inputInformationOfPhoto
