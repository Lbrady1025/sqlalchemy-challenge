# sqlalchemy-challenge

## CWRU Bootcamp Homework Week 10 

This assignment involved using SQLAlchemy to query a SQLite database of weather data from Hawaii. First, using a [Jupyter Notebook](climate_starter.ipynb), the tables from the database were reflected into the SQLAlchemy ORM. From there, an exploratory analysis was performed of the precipitation at all of the included stations for the past year. Below is a bar chart describing this data:

![Precipitation Graph](/Graphs/precip.png)

Next, summary statistics were calculated regarding the amount of recorded precipitation. Finally, a histogram was generated using the temperatures recorded at the most active station:

![Temperature Histogram](/Graphs/hist.png)

Once the exploratory analysis was complete, an API was created using [Python and Flask](app.py). Routes were created for all of the recorded precipitation, the stations at which the data was recorded, temperatures, and start and end dates of observation. 
