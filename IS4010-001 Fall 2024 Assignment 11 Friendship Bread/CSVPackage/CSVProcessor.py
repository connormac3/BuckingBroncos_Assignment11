# CSVProcessor.py

# Name:  Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: dewrm@mail.uc.edu, macfarct@mail.uc.edu, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: 11
# Due Date:  11/21/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:  

# Brief Description of what this module does.  
# Citations: Used ChatGPT for code structure and comments. https://app.zipcodebase.com/documentation
# Anything else that's relevant: None


import csv

class CSVProcessor:
    
    def __init__(self, filename):
        self.__filename = filename
        
    def process(self):
        print("Processing", self.__filename)
        data = self.readData()

    def readData(self):
        return None
        
