# main.py

# Name:  Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: dewrm@mail.uc.edu, macfarct@mail.uc.edu, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: 11
# Due Date:  11/21/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:   This assignment is a group assignment where we are given a csv file that we need to alter to account for animolies and missing data. We have to write the cleaned data to a new csv file along with the anomolies to another csv file  

# Brief Description of what this module does.  This module is used to take the processed data from the CSVProcessor and to make sure that the cleaned data and the anomilies can be sucessfully transfered to their respective files.
# Citations: Used AI for code structure and comments. https://app.zipcodebase.com/documentation
# Anything else that's relevant: None



from API_zipcodePackage.API_zipcode import get_zipcode_data
from CSVPackage.CSVProcessor import *
import os

if __name__ == "__main__":
    print("Starting data cleaning process...")
    # Ensure the Data folder exists
    os.makedirs("Data", exist_ok=True)
    
    # Process fuel purchase data
    csv_processor = CSVProcessor("Data/fuelPurchaseData.csv")
    try:
        csv_processor.process()
        print("Data processing completed successfully.")
    except Exception as e:
        print(f"An error occurred during data processing: {e}")