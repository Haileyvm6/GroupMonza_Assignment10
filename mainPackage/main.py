# main.py

from dataPackage import apidata
from dataPackage.apidata import *
from cleanPackage.clean import *

if __name__ == "__main__":
    city_data = APIdata()
    city_data.get_city_data()