#Author: Steven Broussard                                                                                                                                                       
#Date Created: January 15, 2017                                                                                                                                                 
#Project Name: Familiar Face                                                                                                                                                    
#File Name: driver.py

import facial_recognition
import os
from time import sleep

pathToOutput = "./faceimage.txt"

# method to be called from Java
#def inputFilePath(filePath):
#    inputFile = filePath;

# Listener for new or change of target file

# the while loop is the "listeners"
while not(os.path.exists(pathToOutput)):
    sleep(3)

# once file is found, then "capture" the absolute path to file and activates the readWrite object
# os.system("ls -t | head -1")
readWriteObject = facial_recognition.readWrite(pathToOutput)
inputFileInfo = readWriteObject.readFileInput(pathToOutput)
readWriteObject.writeToFile(inputFileInfo)
