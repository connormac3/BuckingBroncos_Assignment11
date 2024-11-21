# CSVProcessor.py

# Name:  Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: dewrm@mail.uc.edu, macfarct@mail.uc.edu, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: 11
# Due Date:  11/21/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:   This assignment is a group assignment where we are given a csv file that we need to alter to account for animolies and missing data. We have to write the cleaned data to a new csv file along with the anomolies to another csv file  

# Brief Description of what this module does. This module is used to process the CSV data, clean it, and write the cleaned data and anomalies to separate CSV files. It filters the data according to the document and takes out and/or replaces the data that needs to be altered
# Citations: Used AI for code structure and comments. https://app.zipcodebase.com/documentation, 
# Anything else that's relevant: None

import csv
import os
import re
import requests
from concurrent.futures import ThreadPoolExecutor

# API key and base URL for the ZIP code API
API_KEY = "ef749030-a79d-11ef-b0f2-2beeb9ef4d0d"
BASE_URL = "https://app.zipcodebase.com/api/v1/code/city"

def get_zipcode_data(city):
    """ Fetches ZIP code data from the API for the given city.
    Args:
        city (str): The city to fetch ZIP code data for.
    Returns:
        str: A valid ZIP code for the city or None if the lookup fails.
    """
    headers = {"apikey": API_KEY}
    params = (
        ("city", city),
        ("country", "us"),
    )
    
    try:
        # Make a GET request to the API
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        if "results" in data and data["results"]:
            zip_code = data["results"][0]  # Return the first ZIP code in the list
            print(f"Fetched ZIP code: {zip_code} for city: {city}")
            return zip_code
    except requests.exceptions.HTTPError:
        pass
    except requests.exceptions.RequestException:
        pass
    except ValueError:
        pass
    
    return None

class CSVProcessor:
    
    def __init__(self, filename):
        """Initializes the CSVProcessor with the given filename."""
        self.filename = filename
        self.cleaned_data_file = "Data/cleanedData.csv"
        self.anomalies_file = "Data/dataAnomalies.csv"

    def process(self):
        """Reads and processes the CSV file."""
        print("Starting data cleaning process...")
        data = self.read_data()
        if not data:
            raise ValueError("No data to process.")
        
        headers = data[0]  # Extract headers
        rows = data[1:]  # Extract rows
        
        # Ensure headers have ZIP Code column
        if "ZIP Code" not in headers:
            headers.append("ZIP Code")
        
        cleaned_rows = []
        anomalies = []
        seen_rows = set()
        cities_to_fetch = set()
        
        for row in rows:
            # Skip duplicate rows
            row_tuple = tuple(row)
            if row_tuple in seen_rows:
                continue
            seen_rows.add(row_tuple)
            
            # Skip invalid rows
            if len(row) != len(headers) - 1:
                anomalies.append(row)
                continue
            
            row_dict = dict(zip(headers, row + [""]))
   # Skip Pepsi purchases (assuming Pepsi is in the 6th column)
            if row[5].strip().lower() == "pepsi":
                anomalies.append(row)
                continue
            
            # Ensure gross price has 2 decimal places
            try:
                row_dict["Gross Price"] = f"{float(row[2]):.2f}"
            except ValueError:
                anomalies.append(row)
                continue
            
            # Parse Address for city and state (assuming Address is in the 4th column)
            address = row[3]
            city, state = self.extract_city_and_state(address)
            zip_code = row[7].strip() if len(row) > 7 else ""
            if not zip_code:
                cities_to_fetch.add(city)
            
            row_dict["ZIP Code"] = zip_code
            row_dict["City"] = city  # Add city to row_dict for later use
            cleaned_rows.append(row_dict)
        
        # Fetch ZIP codes in parallel
        with ThreadPoolExecutor() as executor:
            city_zip_map = {city: zip_code for city, zip_code in zip(cities_to_fetch, executor.map(get_zipcode_data, cities_to_fetch))}
        
        # Update rows with fetched ZIP codes
        for row_dict in cleaned_rows:
            if not row_dict["ZIP Code"]:
                row_dict["ZIP Code"] = city_zip_map.get(row_dict["City"], "")
        
        # Write cleaned data and anomalies
        self.write_data(self.cleaned_data_file, [headers] + [self.update_row_with_zip(row_dict, headers) for row_dict in cleaned_rows])
        self.write_data(self.anomalies_file, [headers] + anomalies)
        print("Data cleaning process completed.")

    def update_row_with_zip(self, row_dict, headers):
        """Update the row with the new ZIP code in column 8."""
        row_list = [row_dict[header] for header in headers]
        if "ZIP Code" in headers and len(row_list) > 7:
            row_list[7] = row_dict["ZIP Code"]
        return row_list

    def extract_city_and_state(self, address):
        """Extracts city and state from an address string.
        Args:
            address (str): The full address string.
        Returns:
            tuple: A tuple of (city, state), where either can be None.
        """
        match = re.search(r'(.+),\s*([^,]+),\s*([A-Z]{2})', address)
        if not match:
            return None, None
        
        city = match.group(2).strip()
        state = match.group(3).strip()
        
        return city, state

    def read_data(self):
        """Reads data from the CSV file."""
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                return data
        except FileNotFoundError as e:
            print(f"Error reading CSV file: {e}")
            return None

    def write_data(self, filepath, data):
        """Writes data to a CSV file."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        # Ensure the file is created even if data is empty
        if not data:
            with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([])  # Write an empty row to create the file


