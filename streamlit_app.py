import streamlit as st
import folium


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
            "There are currently more than 500 weather alerts nationwide. This seems like a lot, you might want to check local weather."
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
    "The map below will display a state's name, the total active weather alerts and a severity score. The severity score is a weighted calculation for the severity of the weather alerts active in that state and is on a scale of 0 to 1."
)

st.write("")

# create a map of the US
m = folium.Map(location=[39, -96], zoom_start=4)
# create a choropleth map
cp = folium.Choropleth(
    geo_data=state_geo_json,
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

# add a tool tip of the state name, total alerts, and severity score
folium.features.GeoJsonTooltip(
    fields=["name", "severity", "total_alerts"],
    aliases=["State", "Severity Score", "Total Alerts"],
).add_to(cp.geojson)

st.write(m)

st.markdown("Hi, I'm Andrew. Thanks for checking out my app. It's not intended for anything serious, just a demo of the capabilities of Streamlit. I hope you enjoy it!")
st.markdown("Check out this [GitHub repo](https://github.com/andrewkroening/ONWARD-Streamlit-App) or watch the [YouTube demo video](https://youtu.be/8AwRbXZaN1c)")


################################################
# """Code in holding for a future application"""
################################################

# create a dataframe of the state coordinates from the STATE_LIST dictionary
# state_coords_df = pd.DataFrame.from_dict(c.STATE_COORDINATES, orient="index")

# location = st.selectbox("Select a Destination State", c.STATES.keys())

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
