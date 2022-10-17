import streamlit as st
import folium


st.set_page_config(
    page_title="Main Landing",
    page_icon="🛫",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

import pandas as pd
import json
import requests
import nws_tools as nws

# import opensky_tools as opensky
import constants as c


state_df, county_geo = nws.state_data_func()

# create a dataframe of the state coordinates from the STATE_LIST dictionary
state_coords_df = pd.DataFrame.from_dict(c.STATE_COORDINATES, orient="index")

# opensky_count = opensky.count_us_aircraft()


def aircraft_delta(air_data):
    # returns a delta value to show if the number of aircraft is above or below the threshold of 5400
    air_count = air_data
    if air_count >= 5400:
        return "HIGH"
    elif air_count < 5400:
        return "-LOW"


st.title("Welcome to ONWARD")

st.subheader("The OpenSky-National Weather and Aircraft Reporting Dashboard")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.caption("Aircraft in the US")
    # st.metric(
    #     "Total Airborne Flights",
    #     opensky_count,
    #     delta=aircraft_delta(opensky_count),
    #     delta_color="inverse",
    # )

with col2:
    st.metric(
        "Total Weather Alerts",
        state_df["total_alerts"].sum(),
        delta=None,
        delta_color="off",
    )


# location = st.selectbox("Select a Destination State", c.STATES.keys())

# pull in the base US geojson file
url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
us_states = f"{url}/us-states.json"

state_geo = json.loads(requests.get(us_states).text)

# create a map of the US
m = folium.Map(location=[43, -100], zoom_start=4)
# create a choropleth map
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_df,
    columns=["state", "severity_score"],
    key_on="feature.id",
    fill_color="YlOrRd",
    fill_opacity=0.2,
    line_opacity=0.2,
    legend_name="Alert Severity Score",
).add_to(m)

folium.LayerControl().add_to(m)
st.write(m)


"""Code in holding for a future application"""
# # get the state abbreviation for the selected state
# state_abbr = c.STATES[location]
# # get the latitude and longitude for the selected state from the state_coords_df
# state_lat = state_coords_df.loc[state_abbr, "lat"]
# state_long = state_coords_df.loc[state_abbr, "lon"]

# # create a map of the selected state
# m = folium.Map(
#     location=[state_lat, state_long], zoom_start=6, tiles="cartodbpositron"
# )

# colormap = branca.colormap.LinearColormap(
#     vmin=0,
#     vmax=1,
#     colors=["red", "orange", "lightblue", "green", "darkgreen"],
#     caption="Alert Severity",
# )

# folium.GeoJson(
#     county_geo,
#     style_function=lambda x: {
#         "fillColor": colormap(x["properties"]["serverity_score"]),
#         "color": "black",
#         "fillOpacity": 0.4,
#     },
# ).add_to(m)

# # create a choropleth map
# # folium.Choropleth(
# #     geo_data=county_geo,
# #     name="choropleth",
# #     columns=["county", "severity_score", "coordinates"],
# #     fill_color="YlOrRd",
# #     fill_opacity=0.2,
# #     line_opacity=0.2,
# #     legend_name="Alert Severity",
# # ).add_to(m)

# # folium.LayerControl().add_to(m)
# st.write(m)
