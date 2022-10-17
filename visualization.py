"""This is the tool for rendering the map in the streamlit app.

It will take in a dataframe of the weather data and return a map with states color coded by the severiity of alerts and opacity by the number of alerts.

The map will also be able to be filtered by a drop down menu on the main page of the app to center on one state."""

import pandas as pd
import folium
from constants import STATE_COORDINATES, STATES, COLOR_VALUES, BREAKS, COLOR_RANGE


def color_scale(val: float) -> list:
    for i, b in enumerate(BREAKS):
        if val <= b:
            return COLOR_RANGE[i]
    return COLOR_RANGE[i]


def map_visualization(state_data: pd.DataFrame) -> folium.Map:
    """Creates a map of the US with states color coded by the severity of alerts and opacity by the number of alerts.

    Args:
        state_data (pd.DataFrame): A dataframe of the weather data.

    Returns:
        folium.Map: A map of the US with states color coded by the severity of alerts and opacity by the number of alerts.
    """
    # Create the map
    map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Add the states to the map
    for state in STATES.values():
        # Get the data for the state
        state_df = state_data[state_data["state"] == state]
        # Get the number of alerts
        num_alerts = len(state_df)
        # Get the severity of the alerts
        severity = state_df["severity_score"].max()
        # Get the color for the state based using the severity_score and the color_scale function
        color = color_scale(severity)
        # Add the state to the map
        folium.Choropleth(
            geo_data=STATE_COORDINATES[state],
            name=state,
            data=state_df,
            columns=["state", "severity"],
            key_on="feature.id",
            fill_color=color,
            fill_opacity=num_alerts / 10,
            line_opacity=0.2,
            legend_name="Severity of Alerts",
        ).add_to(map)

    return map
