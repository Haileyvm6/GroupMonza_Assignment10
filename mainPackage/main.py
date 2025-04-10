# main.py

from csv import *
from csvPackage.csv import JSONToCSV
from dataPackage.apidata import *
from cleanPackage.clean import *

if __name__ == "__main__":
    api = APIdata()
    api.get_city_data()
    csv = JSONToCSV(api.data)
    csv.convert_to_csv()
