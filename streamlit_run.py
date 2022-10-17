import streamlit as st
import pandas as pd
import geopandas as gpd
import altair as alt

import nws_tools as nws
import opensky_tools as opensky


st.set_page_config(
    page_title="Welcome to NOAH - The NWS-OpenSky Alamgamated Hub",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("Test")

# Header, Subheader, and Caption will be useful

# st.button for the refresh data button

# st.metric(label, value, delta=None, delta_color="normal", help=None) for the total flights

# st.map(data=None, zoom=None, use_container_width=True) for the map

# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible") for what state you are looking at

# st.sidebar for the sidebar to show aggregate data unless a state is selected, then show state data

# st.spinner(text="In progress...") just because


st.map()
