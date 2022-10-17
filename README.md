# ONWARD - The OpenSky-National Weather and Aircraft Reporting Dashboard

### Introduction

#### Hi there! Welcome to this project. Below is a little map of what I'm trying to do here. This project is intended to exercise a few different things I've never done before, so the engineering might not make total sense.

#### Here's a little sketch of what I'm trying to accomplish. The general theme is that I'm going to construct several microservices and then attempt to string them together to accomplish some data engineering tasks. The final output should be some kind of interface that returns some indicators about the potential status of a flight that day

![alt text](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/little_tools/Roadmap.png?raw=true)

#### I'm currently working on Phase II of the project

* Build a simple web app to deploy through the Streamlit cloud service.
* Added a tool to query OpenSky for flight counts. You can find it [here.](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/opensky_tools.py)
* Modified the existing tools to add additional formats for future features.

#### Here's what Phase I that looked like with a [demo video here](https://youtu.be/RnMwroCijJQ)

* Downloaded a [dataset from Kaggle](https://www.kaggle.com/datasets/ryanjt/airline-delay-cause) that details roughly 20 years of airline flight delay.
* Used a [Jupyter Notebook to do some EDA](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/eda/Airline_Delay_EDA.ipynb) on that dataset. Concluded that delays spike in the summer and around the winter holidays (shocking, I know)
* Built a tool to query the National Weather Service for all active weather alerts. Get it from [nws_tools](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/nws_tools.py)
* I used a databricks cluster to temporarily house the data, but have since depreciated that feature because it was overkill for how much data we have here.

#### If you are more of a visual person, here's a little sketch of the first chunk of the project

![alt text](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/little_tools/Phase_I.png?raw=true)
