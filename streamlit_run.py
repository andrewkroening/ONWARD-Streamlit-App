import streamlit as st
import streamlit_folium as st_folium
import folium


st.set_page_config(
    page_title="Main Landing",
    page_icon="🛫",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

import pandas as pd

import nws_tools as nws
import opensky_tools as opensky
import constants as c
import visualization as viz

# Header, Subheader, and Caption will be useful

# st.button for the refresh data button

# st.metric(label, value, delta=None, delta_color="normal", help=None) for the total flights

# st.map(data=None, zoom=None, use_container_width=True) for the map

# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible") for what state you are looking at

# st.sidebar for the sidebar to show aggregate data unless a state is selected, then show state data

# st.spinner(text="In progress...") just because


def state_data():
    """Gets state data"""
    # get the latest compiled weather alerts
    state_data = nws.compiled_alerts()
    return state_data


def aircraft_data():
    # get the latest aircraft data
    open_data = opensky.count_us_aircraft()
    return open_data


def aircraft_delta(air_data):
    # returns a delta value to show if the number of aircraft is above or below the threshold of 5400
    air_count = air_data
    if air_count >= 5400:
        return "HIGH"
    elif air_count < 5400:
        return "-LOW"


st.title("Welcome to NOAH")

st.subheader("The NWS-OpenSky Alamgamated Hub")

st.button("Refresh Data", on_click=aircraft_data)

st.metric(
    "Airborne Flights",
    aircraft_data(),
    delta=aircraft_delta(aircraft_data()),
    delta_color="inverse",
)

st.selectbox("Select a State", c.STATES.keys())

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
m

# convert the STATE_COORDINATES dictionary to a dataframe
state_df = pd.DataFrame.from_dict(
    c.STATE_COORDINATES, orient="index", columns=["state", "lat", "lon"]
)

# merge the state_data and state_df dataframes on the state column
state_wx_and_loc = state_df.merge(state_data(), on="state")

# drop alaska and hawaii from the dataframe
state_wx_and_loc = state_wx_and_loc[
    (state_wx_and_loc["state"] != "AK") & (state_wx_and_loc["state"] != "HI")
]

# create a map of the U.S. with the number of alerts for each state
st.map(state_wx_and_loc)
