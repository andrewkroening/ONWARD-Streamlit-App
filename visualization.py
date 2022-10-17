"""This is the tool for rendering the map in the streamlit app.

It will take in a dataframe of the weather data and return a map with states color coded by the severiity of alerts and opacity by the number of alerts.

The map will also be able to be filtered by a drop down menu on the main page of the app to center on one state."""

import pandas as pd
import folium
from constants import STATE_COORDINATES, STATES, COLOR_VALUES, BREAKS, COLOR_RANGE


def m():
    url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    state_geo = f"{url}/us-states.json"
    state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
    state_data = pd.read_csv(state_unemployment)

    map = folium.Map(location=[48, -102], zoom_start=3)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["State", "Unemployment"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Unemployment Rate (%)",
    ).add_to(map)

    folium.LayerControl().add_to(map)

    return map


# # Get the color range for the map
# def color_scale(val: float) -> list:
#     for i, b in enumerate(BREAKS):
#         if val <= b:
#             return COLOR_RANGE[i]
#     return COLOR_RANGE[i]


# # Make the map
# def make_map(
#     geo_df: pd.DataFrame,
#     df: pd.DataFrame,
#     map_feature: str,
#     data_format: str = "Raw Values",
#     show_transit: bool = False,
# ):
#     """This function will render the map for the app."""

#     pass


# m = folium.Map(location=[48, -102], zoom_start=3)

# folium.Choropleth(
#     geo_data=state_geo,
#     name="choropleth",
#     data=state_data,
#     columns=["State", "Unemployment"],
#     key_on="feature.id",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Unemployment Rate (%)",
# ).add_to(m)

# folium.LayerControl().add_to(m)

# m
