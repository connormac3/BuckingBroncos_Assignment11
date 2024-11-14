# CSVProcessor.py

# Name: Ryan Dew,
# email: dewrm@mail.uc.edu, 
# Assignment Number: 08
# Due Date:  10/31/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This is a team assignment that we are told to collaborate on a python project, we chose to create a sports team matchup program. We have 3 classes 1 for team wins and losses, 1 for total points score and 1 change team name.

# Brief Description of what this module does. This module is a class that models a team matchup, including the opponent's name and the location of the game. It provides methods to get and set these attributes, print matchup details, and represent the object as a string.
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
        
