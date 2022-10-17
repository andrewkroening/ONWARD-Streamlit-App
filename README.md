
# Airline Delay Information Project

### Introduction

#### Hi there! Welcome to this project. Below is a little map of what I'm trying to do here. This project is intended to exercise a few different things I've never done before, so the engineering might not make total sense...

#### Here's a little sketch of what I'm trying to accomplish. The general theme is that I'm going to construct several microservices and then attempt to string them together to accomplish some data engineering tasks. The final output should be some kind of interface that returns some indicators about the potential status of a flight that day.

![alt text](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/little_tools/Roadmap.png?raw=true)

#### I'm currently working on Phase II of the project.

* Built a CI/CD pipeline that deploys a docker image direct to [DockerHub](https://hub.docker.com/repository/docker/ajkroening/flight-delay-project-fall22) everytime a change is pushed to the repository.
* Added a tool to query OpenSky for flight numbers. You can find it [here.](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/opensky_tools.py)
* Rebuilt the user interface as a [FastAPI Web App.](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/main.py)

#### Here's what Phase I that looked like with a [demo video here](https://youtu.be/RnMwroCijJQ):

* Downloaded a [dataset from Kaggle](https://www.kaggle.com/datasets/ryanjt/airline-delay-cause) that details roughly 20 years of airline flight delay.
* Used a [Jupyter Notebook to do some EDA](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/eda/Airline_Delay_EDA.ipynb) on that dataset. Concluded that delays spike in the summer and around the winter holidays (shocking, I know)
* Built a tool to query the National Weather Service for all active weather alerts. Get it from [nws_tools](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/nws_tools.py)
* Used a tool to transform the payload for easier SQL table loading. Get it from [nws_tools](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/nws_tools.py)
* Built a Databricks cluster
* Built a tool to build a SQL table in Databricks that would accept the NWS payload. Get it from [databricks_tools](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/databricks_tools.py)
* Built some basic, descriptive functions to give simple info about how many alerts there are according to the NWS and the table in Databricks. The [cli_tool](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/logic/cli_nws_query.py) is where you'll find them.

#### If you are more of a visual person, here's a little sketch of the first chunk of the project.

![alt text](https://github.com/nogibjj/Flight-Delay-Project-Kroening/blob/fe7e31c6376132588065c531f956ed9b95173954/little_tools/Phase_I.png?raw=true)
