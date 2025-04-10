
# File Name : apidata.py
# Student Name: Joshua Slocumb, Abel Yemaneab, Hailey Manuel, Richie James
# email:  slocumjt@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment:This Assignment accesses an API containing informaiton about cities in the US and prints some information about them
# Brief Description of what this module does. This module accesses the API using a key and brings back the rough data
# Citations: Rapid API
import json
import requests

class APIdata:


    def __init__(self):
        pass
            
    def get_city_data(self):
            response = requests.get('https://wft-geo-db.p.rapidapi.com/v1/geo/cities?countryIds=US&limit=10&sort=-population', 
                                headers={
                                    'X-RapidAPI-Key': '4cc88cdf7cmshf7b29940764088ap104c7ajsnb09745931509',
                                    'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com'
                                })

            json_string = response.content

            parsed_json = json.loads(json_string) # Now we have a python dictionary

            total = int(parsed_json['metadata']['totalCount']) # The number of cities that were returned

            for city in parsed_json['data']:
                print(city)


