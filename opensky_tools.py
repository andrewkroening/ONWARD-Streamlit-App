"""Create a module to handle the OpenSky API"""

import requests
import json


def get_opensky_data():
    """Get the data from the OpenSky API"""
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url, timeout=5)
    data = response.json()
    # If the response is not 200, return an empty dictionary
    if response.status_code != 200:
        return {}
    return data


# define a function to count the number of aircraft over the US
def count_us_aircraft():
    """Count the number of aircraft over the US"""
    data = get_opensky_data()
    us_aircraft = 0
    for aircraft in data["states"]:
        if aircraft[5] is not None and aircraft[6] is not None:
            if (
                aircraft[6] > 24.660845
                and aircraft[6] < 49.189787
                and aircraft[5] > -124.848974
                and aircraft[5] < -66.885444
            ):
                us_aircraft += 1
    return us_aircraft


if __name__ == "__main__":
    print(count_us_aircraft())
