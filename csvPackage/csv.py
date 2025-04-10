# csv.py
# File Name : apidata.py
# Student Name: Joshua Slocumb, Abel Yemaneab, Hailey Manuel, Richie James
# email:  slocumjt@mail.uc.edu, yemaneag@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment:This Assignment accesses an API containing informaiton about cities in the US and prints some information about them
# Brief Description of what this module does. This module accesses the API using a key and brings back the rough data
# Citations: https://www.geeksforgeeks.org/convert-json-to-csv-in-python/, https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv

import csv
from dataPackage import *
class JSONToCSV:
    def __init__(self, data):
        self.data = data
    
    def convert_to_csv(self, output_file='cities_data.csv'):
        
   
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'countryCode', 'latitude', 'longitude', 'population'])

            writer.writeheader()

            for city in self.data:
                writer.writerow({
                    'id': city.get('id'),
                    'name': city.get('name', city.get('city', '')), 
                    'countryCode': city.get('countryCode'),
                    'latitude': city.get('latitude'),
                    'longitude': city.get('longitude'),
                    'population': city.get('population')
                })

        print(f"CSV file '{output_file}' created successfully.")
        

