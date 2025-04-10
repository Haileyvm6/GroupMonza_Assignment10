
# File Name : clean.py
# Student Name: Joshua Slocumb, Abel Yemaneab, Hailey Manuel, Richie James
# email:  slocumjt@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment:This Assignment accesses an API containing informaiton about cities in the US and prints some information about them
# Brief Description of what this module does. This module cleans our data we get from the API
# Citations: Rapid API

from dataPackage import *
import json

class cleandata:

    def clean_city_data(parsed_json):
        """Extract city name, country, and population from raw JSON data"""
        clean_data =[]

        for city in parsed_json['data']:
            name = city.get('name')
            country = city.get('country')
            latitude = city.get('latitude')
            clean_data.append({
                'name' : name,
                'country' :country,
                'latitude': latitude
                })
               
        return clean_data
    def save_to_json(data, filename='cleaned_cities.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Cleaned data saved to{filename}")
 

