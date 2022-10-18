"""Module of functions to query the NWS database for active alerts"""

# write a tool that gets all active alerts from the NWS
# return a JSON and print the number of active alerts

import requests
import pandas as pd
import json
from constants import STATE_LIST

url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
us_states = f"{url}/us-states.json"

state_geo = json.loads(requests.get(us_states).text)


def get_alerts():
    """Return a JSON payload of all active alerts"""
    # define the URL for the NWS API
    url = "https://api.weather.gov/alerts/active"
    # send the request to the NWS API
    response = requests.get(url, timeout=5)
    # return the response from the NWS API
    return response.json()


def package_alerts(json):
    """Transform the resulting JSON payload into an easier to manipulate version"""
    # get the JSON object from the NWS API
    json_object = json
    # keep the severity, certainty, last two characters, and coordinates of the senderName as a pandas dataframe
    alert_df = pd.DataFrame(
        [
            [
                x["properties"]["severity"],
                x["properties"]["senderName"][-2:],
            ]
            for x in json_object["features"]
        ],
        columns=["severity", "senderName"],
    )
    # drop rows where the senderName is "WS"
    alert_df = alert_df[alert_df["senderName"] != "WS"]
    # add an index column with new index values
    alert_df = alert_df.reset_index(drop=True)
    # return the dataframe
    return alert_df


def compiled_alerts(alert_df):
    """Return a dataframe with alerts condensed to provide state-level information"""
    state_alerts_df = alert_df
    # Iterate over states and create a new dataframe with the number of alerts by severity
    state_alerts_df = pd.DataFrame(
        [
            [
                state,
                len(state_alerts_df[state_alerts_df["senderName"] == state]),
                len(
                    state_alerts_df[
                        (state_alerts_df["senderName"] == state)
                        & (state_alerts_df["severity"] == "Extreme")
                    ]
                ),
                len(
                    state_alerts_df[
                        (state_alerts_df["senderName"] == state)
                        & (state_alerts_df["severity"] == "Severe")
                    ]
                ),
                len(
                    state_alerts_df[
                        (state_alerts_df["senderName"] == state)
                        & (state_alerts_df["severity"] == "Moderate")
                    ]
                ),
                len(
                    state_alerts_df[
                        (state_alerts_df["senderName"] == state)
                        & (state_alerts_df["severity"] == "Minor")
                    ]
                ),
            ]
            for state in state_alerts_df["senderName"].unique()
        ],
        columns=[
            "state",
            "total_alerts",
            "extreme_alerts",
            "severe_alerts",
            "moderate_alerts",
            "minor_alerts",
        ],
    )
    # add a column with the total alerts divided by 100
    state_alerts_df["total_alerts_per_100"] = (
        state_alerts_df["total_alerts"] / 100
    ).round(2)
    # if the total alerts per 100 is above 0.99, set it to 0.99
    state_alerts_df["total_alerts_per_100"] = state_alerts_df[
        "total_alerts_per_100"
    ].apply(lambda x: 0.99 if x > 0.99 else x)
    # add a column to provide a severity score
    state_alerts_df["severity_score"] = (
        state_alerts_df["extreme_alerts"] * 5
        + state_alerts_df["severe_alerts"] * 3.5
        + state_alerts_df["moderate_alerts"] * 2
        + state_alerts_df["minor_alerts"] * 0.5
    )
    # normalize the alert severity_score by reducing scores over 99 to 99 and then dividing by 100
    state_alerts_df["severity_score"] = (
        state_alerts_df["severity_score"].apply(lambda x: 99 if x > 99 else x) / 100
    )
    # add missing states from teh constants States list with all zeroes
    for state in STATE_LIST:
        if state not in state_alerts_df["state"].values:
            state_alerts_df = state_alerts_df.append(
                {
                    "state": state,
                    "total_alerts": 0,
                    "extreme_alerts": 0,
                    "severe_alerts": 0,
                    "moderate_alerts": 0,
                    "minor_alerts": 0,
                    "total_alerts_per_100": 0,
                    "severity_score": 0,
                },
                ignore_index=True,
            )
    # return the dataframe
    return state_alerts_df


def county_geo_json(json):
    """Return a GeoJSON payload of all county level alerts"""
    # use the JSON payload from the get_alerts function
    alert_json = json
    # loop through the alert_json and create a geojson object using the same file structure as the state-geos.json file in the data directory
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": x["geometry"],
                "properties": {
                    "state": x["properties"]["senderName"][-2:],
                    "severity": x["properties"]["severity"],
                },
            }
            for x in alert_json["features"]
        ],
    }
    # add a severity score to each alert
    for feature in geojson["features"]:
        if feature["properties"]["severity"] == "Extreme":
            feature["properties"]["severity_score"] = 0.9
        elif feature["properties"]["severity"] == "Severe":
            feature["properties"]["severity_score"] = 0.7
        elif feature["properties"]["severity"] == "Moderate":
            feature["properties"]["severity_score"] = 0.5
        elif feature["properties"]["severity"] == "Minor":
            feature["properties"]["severity_score"] = 0.2
        else:
            feature["properties"]["severity_score"] = 0
    # if geometry is None, add the geometry from the state_geo json file for the state
    for feature in geojson["features"]:
        if feature["geometry"] is None:
            for state in state_geo["features"]:
                if state["id"] == feature["properties"]["state"]:
                    feature["geometry"] = state["geometry"]
    # return the geojson
    return geojson


def state_data_func():
    """This is the function to compile all state data and return the associated objects for the app"""
    all_alerts = get_alerts()
    alerts_df = package_alerts(all_alerts)
    state_alerts_df = compiled_alerts(alerts_df)
    county_geo_alerts = county_geo_json(all_alerts)

    return state_alerts_df, county_geo_alerts


if __name__ == "__main__":
    state_data_func()
