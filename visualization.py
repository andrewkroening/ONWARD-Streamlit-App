"""This is the tool for rendering the map in the streamlit app.

It will take in a dataframe of the weather data and return a map with states color coded by the severiity of alerts and opacity by the number of alerts.

The map will also be able to be filtered by a drop down menu on the main page of the app to center on one state."""

import pandas as pd
from constants import STATE_COORDINATES, STATES, COLOR_VALUES, BREAKS, COLOR_RANGE

# Get the color range for the map
def color_scale(val: float) -> list:
    for i, b in enumerate(BREAKS):
        if val <= b:
            return COLOR_RANGE[i]
    return COLOR_RANGE[i]


# Make the map
def make_map(
    geo_df: pd.DataFrame,
    df: pd.DataFrame,
    map_feature: str,
    data_format: str = "Raw Values",
    show_transit: bool = False,
):
    """This function will render the map for the app."""

    pass
