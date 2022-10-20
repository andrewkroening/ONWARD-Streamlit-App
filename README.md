# ONWARD - The OpenSky-National Weather and Aircraft Reporting Dashboard

[![Continuous Integration](https://github.com/andrewkroening/ONWARD-Streamlit-App/actions/workflows/main.yml/badge.svg)](https://github.com/andrewkroening/ONWARD-Streamlit-App/actions/workflows/main.yml)

### Introduction

 Hi there! Welcome to this project. Below is a little map of what I'm trying to do here. This project is intended to exercise a few different things I've never done before, so the engineering might not make total sense

#### If you are looking for the most recent version of [ONWARD, click here.](https://onward.streamlitapp.com/)

 Here's a little sketch of what I'm trying to accomplish. The general theme is that I'm going to construct several microservices and then attempt to string them together to accomplish some data engineering tasks. The final output should be some kind of interface that returns some indicators about the potential status of a flight that day

![alt text](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/0faa42f9fd5ff6ba68067c99ef84cf423a945e9a/little_tools/Project_roadmap.png?raw=true)

#### I'm currently working on Phase III of the project

* Refine the map interface to provide better insights.
* Allow users to select a destination for insights.
* Provide a top level delay estimator.

#### Here's what Phase II consisted of and a [demo video here](https://youtu.be/8AwRbXZaN1c)

* Build a simple web app to deploy through the [Streamlit cloud service.](https://onward.streamlitapp.com/)
* Added a tool to query OpenSky for flight counts. You can find it [here.](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/0faa42f9fd5ff6ba68067c99ef84cf423a945e9a/opensky_tools.py)
* Modified the existing tools to add additional formats for future features.
* Added a [constants](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/0faa42f9fd5ff6ba68067c99ef84cf423a945e9a/constants.py) to house some specific variables that I used throughout.
* Added a [data directory](https://github.com/andrewkroening/ONWARD-Streamlit-App/tree/main/data) for some specific data sources that built the map visual in the app and will be necessary for future features.
* Built a small module to transform a GeoJSON of state data and add weather alert info for rendering. That tool is called [state JSON transform.](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/a63352dc1888fa3588b093c962474b599f9f4d98/state_json_transform.py)

#### Here's what Phase I looked like with a [demo video here](https://youtu.be/RnMwroCijJQ)

* Downloaded a [dataset from Kaggle](https://www.kaggle.com/datasets/ryanjt/airline-delay-cause) that details roughly 20 years of airline flight delays.
* Used a [Jupyter Notebook to do some EDA](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/0faa42f9fd5ff6ba68067c99ef84cf423a945e9a/eda/Airline_Delay_EDA.ipynb) on that dataset. Concluded that delays spike in the summer and around the winter holidays (shocking, I know).
* Built a tool to query the National Weather Service for all active weather alerts. Get it from [nws_tools.](https://github.com/andrewkroening/ONWARD-Streamlit-App/blob/0faa42f9fd5ff6ba68067c99ef84cf423a945e9a/nws_tools.py)
* I used a databricks cluster to temporarily house the data, but have since depreciated that feature because it was overkill for how much data we have here.

#### If you are more of a visual person, here's a little sketch of the first chunk of the project before it was overhauled to build the Streamlit App.

![alt text](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/little_tools/Phase_I.png?raw=true)
