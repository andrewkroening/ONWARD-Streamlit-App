"""Module to transform a geo JSON file of the states"""

import json
import requests


def state_geo_json_transform(df):
    """Return a GeoJSON payload of all the 50 states with their severity scores and total alert counts

    Requires a dataframe with the following columns at min: state, severity_score, total_alerts"""

    # pull in the base US geojson file
    url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    us_states = f"{url}/us-states.json"

    state_geo = json.loads(requests.get(us_states).text)

    # loop through the state geo and add the severity score and total alerts from the state_df to the properties
    for state in state_geo["features"]:
        state_name = state["id"]
        for s in df.state:
            if state_name == s:
                state["properties"]["severity"] = df[df["state"] == state_name][
                    "severity_score"
                ].values[0]
        for s in df.state:
            if state_name == s:
                # add the total alerts as a float to the properties
                state["properties"]["total_alerts"] = float(
                    df[df["state"] == state_name]["total_alerts"].values[0]
                )
    return state_geo


if __name__ == "__main__":
    # import the state_df
    import nws_tools

    df, df2 = nws_tools.state_data_func()
    # run the function
    state_geo_json_transform(df)
