# SQLAlchemy-Challenge

The Climate Analysis directory contains these files:

	* climate_starter.ipynb	
	* app.py
	* Resources directory which contains two csv files and a sqllite file

The climate_starter jupyter notebook file contains weather analysis from the data provided in the two csv files. The analysis steps are shown below.

	1. Design a query to retrieve the last 12 months of precipitation data (only retrieving the date and precipitation values)
	
	2. Load the query results into a Pandas DataFrame, set the index to the date column, and sort the DataFrame values by `date`
	
	3. Plot the results on a bar chart
	
	4. Design a query to calculate the total number of stations and find the most active stations (list the stations and observation counts in descending order)
	
	5. Design a query to retrieve the last 12 months of temperature observation data filtering only the most active station
	
	6. Plot the results as a histogram

The app python file contains code that creates a Flask API based on the queries designed in the jupyter notebook. The Flask routes are shown below.

	* Home page: List all routes that are available
	
	* `/api/v1.0/precipitation`: Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
						  Return the JSON representation of your dictionary.
	
	* `/api/v1.0/stations`: Return a JSON list of stations from the dataset
	
	* `/api/v1.0/tobs`: Query the dates and temperature observations of the most active station for the last year of data.
				    Return a JSON list of temperature observations (TOBS) for the previous year.
	
	* `/api/v1.0/<start>`: Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
					 When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
					 
  	* `/api/v1.0/<start>/<end>': Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  	                            When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

