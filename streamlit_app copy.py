import streamlit as st
import folium
import branca
import pandas as pd


st.set_page_config(
    page_title="ONWARD",
    page_icon="🛫",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

import nws_tools as nws
import opensky_tools as opensky
import state_json_transform as state_json

# import constants as c

state_df, county_geo = nws.state_data_func()

state_geo_json = state_json.state_geo_json_transform(state_df)

airports = pd.read_csv("data/airports.csv")

# unpack the county geo as a data frame called county_colors with an index number  and a severity and severity score column from the properties
county_colors = (
    pd.DataFrame(county_geo["features"]).properties.apply(pd.Series).reset_index()
)

opensky_count = opensky.count_us_aircraft()


def aircraft_delta(air_data):
    # returns a delta value to show if the number of aircraft is above or below the threshold of 5400
    air_count = air_data
    if air_count >= 5400:
        return "HIGH"
    elif air_count < 5400:
        return "-LOW"


st.title("Welcome to ONWARD")

st.subheader("The OpenSky-National Weather and Aircraft Reporting Dashboard")

col1, col2 = st.columns((1, 3))

col3, col4 = st.columns((1, 3))

with col1:
    st.metric(
        "Total Airborne Flights",
        opensky_count,
        delta=None,
        delta_color="off",
    )

with col2:
    if opensky_count > 5400:
        st.error(
            "There are currently more than 5400 aircraft in the air. This is above some upper threshold the FAA thinks makes for a busy sky."
        )
    elif opensky_count > 5000:
        st.warning(
            "There are currently more than 5000 aircraft in the air. This is getting crowded."
        )
    else:
        st.success(
            "There are currently less than 5000 aircraft in the air. The skies don't look too busy."
        )


with col3:
    st.metric(
        "Total Weather Alerts",
        state_df["total_alerts"].sum(),
        delta=None,
        delta_color="off",
    )

with col4:
    if state_df["total_alerts"].sum() > 600:
        st.error(
            "There are currently more than 600 weather alerts nationwide. This seems like a lot, you might want to check local weather."
        )
    elif state_df["total_alerts"].sum() > 500:
        st.warning(
            "There are currently more than 500 weather alerts nationwide. This seems like a lot, you might want to check local weather."
        )
    else:
        st.success(
            "There are currently less than 500 weather alerts nationwide. This seems like a good day to fly."
        )

st.write("")

st.subheader("Current Weather Alerts by State")

st.caption(
    "The map below will show the current weather alearts active in the United States. The color density and color give a clue to the severity and volume."
)

st.write("")

####################
#### Map Writer ####
####################

# set the colorscale using a branca colormap
colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 1)

# define a style function that takes a feature and returns a style dictionary
def style_function(feature):
    # get the severity score from the feature properties
    severity_score = feature["properties"]["severity_score"]
    # get the color for the severity score
    color = colorscale(severity_score)
    # return a style dictionary
    return {"fillColor": color, "color": "black", "weight": 1, "fillOpacity": 0.05}


# create a map of the US
m = folium.Map(location=[39, -96], tiles="cartodbpositron", zoom_start=4)

# add the airports to the map
# for i in range(0, len(airports)):
#     folium.Marker(
#         location=[airports.iloc[i]["latitude"], airports.iloc[i]["longitude"]],
#         popup=airports.iloc[i]["name"],
#         icon=folium.Icon(color="blue", icon="plane"),
#     ).add_to(m)

# add the geojson to the map
gj = folium.GeoJson(
    county_geo,
    name="geojson",
    style_function=style_function,
    zoom_on_click=True,
).add_to(m)

st.write(m)

st.write("------")
st.markdown("")
st.markdown(
    "Hi, I'm Andrew. Thanks for checking out my app. It's not intended for anything serious, just a demo of the capabilities of Streamlit. I hope you enjoy it!"
)
st.markdown(
    "Check out the [GitHub repo](https://github.com/andrewkroening/ONWARD-Streamlit-App) or watch the [YouTube demo video](https://youtu.be/8AwRbXZaN1c) here. Cheers!"
)
