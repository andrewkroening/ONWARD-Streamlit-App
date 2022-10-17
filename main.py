"""Web App to deploy the tools through an AWS Container...Eventually"""

from fastapi import FastAPI
import uvicorn
import geopandas as gpd

# import requests

from nws_tools import get_alerts, package_alerts, alert_info, alerts_for_state
from opensky_tools import count_us_aircraft, get_opensky_data

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to this flight informaiton app. Please use the /docs endpoint to see the available endpoints."



# ask the user for a destination state and return the number of weather alerts for that state by severity
@app.get("/status/{state}")
def read_opensky_count(state: str):
    output = count_us_aircraft()
    # get the number of extreme alerts for a given state
    extreme_alerts = len(
        alerts_for_state(state)[alerts_for_state(state)["severity"] == "Extreme"]
    )
    # get the number of severe alerts for a given state
    severe_alerts = len(
        alerts_for_state(state)[alerts_for_state(state)["severity"] == "Severe"]
    )
    # get the number of moderate alerts for a given state
    moderate_alerts = len(
        alerts_for_state(state)[alerts_for_state(state)["severity"] == "Moderate"]
    )
    # get the number of minor alerts for a given state
    minor_alerts = len(
        alerts_for_state(state)[alerts_for_state(state)["severity"] == "Minor"]
    )
    # get the number of unknown alerts for a given state
    unknown_alerts = len(
        alerts_for_state(state)[alerts_for_state(state)["severity"] == "Unknown"]
    )
    if output > 5400:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's alot! It is more than the count of 5400 that the FAA says is the upper threshold for traffic. \n\n For the state of "
            + state
            + " there are currently "
            + str(extreme_alerts)
            + " extreme,"
            + str(severe_alerts)
            + " severe,"
            + str(moderate_alerts)
            + " moderate,"
            + str(minor_alerts)
            + " minor, and "
            + str(unknown_alerts)
            + " unknown alerts."
        )
    elif output > 4750:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's getting to be alot! It is less than the count of 5400 that the FAA says is the upper threshold for traffic.  \n\n For the state of "
            + state
            + " there are currently "
            + str(extreme_alerts)
            + " extreme,"
            + str(severe_alerts)
            + " severe,"
            + str(moderate_alerts)
            + " moderate,"
            + str(minor_alerts)
            + " minor, and "
            + str(unknown_alerts)
            + " unknown alerts."
        )
    else:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's not alot. For the state of "
            + state
            + " there are currently "
            + str(extreme_alerts)
            + " extreme,"
            + str(severe_alerts)
            + " severe,"
            + str(moderate_alerts)
            + " moderate,"
            + str(minor_alerts)
            + " minor, and "
            + str(unknown_alerts)
            + " unknown alerts."
        )


# run the app
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
