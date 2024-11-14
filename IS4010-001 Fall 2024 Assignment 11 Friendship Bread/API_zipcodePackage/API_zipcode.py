# API_zipcode.py

# Name: Ryan Dew
#API_zipcode.py

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


import requests

headers = { 
  "apikey": "aa80fb00-a28a-11ef-8fc3-573b5fa4625f"}

params = (
   ("codes","10005,51503"),
);

response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params);
print(response.text)