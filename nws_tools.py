"""Module of functions to query the NWS database for active alerts"""

# write a tool that gets all active alerts from the NWS
# return a JSON and print the number of active alerts

import requests
import pandas as pd


def get_alerts():
    """Return a JSON payload of all active alerts"""
    # define the URL for the NWS API
    url = "https://api.weather.gov/alerts/active"
    # send the request to the NWS API
    response = requests.get(url, timeout=5)
    # return the response from the NWS API
    return response.json()


def package_alerts():
    """Transform the resulting JSON payload into an easier to manipulate version"""
    # get the JSON object from the NWS API
    json_object = get_alerts()
    # keep the severity, certainty, last two characters, and coordinates of the senderName as a pandas dataframe
    alert_df = pd.DataFrame(
        [
            [
                x["properties"]["severity"],
                x["properties"]["certainty"],
                x["properties"]["senderName"][-2:],
            ]
            for x in json_object["features"]
        ],
        columns=["severity", "certainty", "senderName"],
    )
    # drop rows where the senderName is "WS"
    alert_df = alert_df[alert_df["senderName"] != "WS"]
    # add an index column with new index values
    alert_df = alert_df.reset_index(drop=True)
    # return the dataframe
    return alert_df


def compiled_alerts():
    """Return a dataframe with alerts condensed to provide state-level information"""
    state_alerts_df = package_alerts()
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
    # add a column to provide a severity score
    state_alerts_df["severity_score"] = (
        state_alerts_df["extreme_alerts"] * 5
        + state_alerts_df["severe_alerts"] * 3.5
        + state_alerts_df["moderate_alerts"] * 2
        + state_alerts_df["minor_alerts"] * 0.5
    )
    # return the dataframe
    return state_alerts_df


# these two functions are for testing purposes and will be removed later


def alert_info():
    """Get basic summary stats from the alerts"""
    # get the df object from the NWS API
    alert_df = package_alerts()
    # print the total number of alerts
    print("Total number of alerts: ", len(alert_df))
    # print the number of active alerts from senderName "WS"
    print("National-Level Alerts: ", len(alert_df[alert_df["senderName"] == "WS"]))
    # print the number of active alerts after dropping rows where the senderName is "WS"
    print("State-Level Alerts: ", len(alert_df[alert_df["senderName"] != "WS"]))
    # print number of extreme alerts
    print("Extreme Alerts: ", len(alert_df[alert_df["severity"] == "Extreme"]))
    # print the five states with the most active alerts
    print(
        "States with the most active alerts: \n",
        alert_df["senderName"].value_counts().head(),
    )


def alerts_for_state(state):
    """Return a dataframe of all active alerts for a given state"""
    # get the df object from the NWS API
    alert_df = package_alerts()
    # return a count of the number of alerts by severity for a given state
    return alert_df[alert_df["senderName"] == state]
