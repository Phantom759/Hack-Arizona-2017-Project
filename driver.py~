#Author: Steven Broussard                                                                                                                                                       
#Date Created: January 15, 2017                                                                                                                                                 
#Project Name: Familiar Face                                                                                                                                                    
#File Name: driver.py

import facial_recognition
from os import path
from os import remove
from time import sleep

inputFile = "./input.txt"

# Listener for new or change of target file

# the while loop is the "listeners"
while not(path.exists(inputFile)):
    sleep(3)

# once file is found, then activates the readWrite object
readWriteObject = facial_recognition.readWrite(inputFile)
inputFileInfo = readWriteObject.readFileInput(inputFile)
readWriteObject.writeToFile(inputFileInfo)

# delete the input file
remove(inputFile)
