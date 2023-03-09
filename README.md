# sqlalchemy-challenge
## Purpose
Analyze and Explore Climate Data and Design a Climate App.
## Overview
The goal of this challenge is to do climate analysis on Honolulu, Hawaii using Python, ORM queries, Pandas, Matplotlib and SQLAlchemy. To do a basic climate analysis and data exploration of the climate database. The items to do are listed below.
### Jupyter Notebook Database Connection
- [x] Use the SQLAlchemy create_engine() function to connect to your SQLite database
- [x] Use the SQLAlchemy automap_base() function to reflect your tables into classes
- [x] Save references to the classes named station and measurement
- [x] Link Python to the database by creating a SQLAlchemy session
- [x] Close your session at the end of your notebook
### Precipitation Analysis
- [x] Create a query that finds the most recent date in the dataset (8/23/2017)
- [x] Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable
- [x] Save the query results to a Pandas DataFrame to create date and precipitation columns
- [x] Sort the DataFrame by date
- [x] Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables
- [x] Use Pandas to print the summary statistics for the precipitation data
### Station Analysis
- [x] Design a query that correctly finds the number of stations in the dataset (9)
- [x] Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)
- [x] Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)
- [x] Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations
- [x] Save the query results to a Pandas DataFrame
- [x] Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count.
### API SQLite Connection & Landing Page
Flask application must:
- [x] Correctly generate the engine to the correct sqlite file
- [x] Use automap_base() and reflect the database schema
- [x] Correctly save references to the tables in the sqlite file (measurement and station)
- [x] Correctly create and binds the session between the python app and database
- [x] Display the available routes on the landing page
### API Static Routes
Flask application must include:

A precipitation route that:
- [x] Returns json with the date as the key and the value as the precipitation
- [x] Only returns the jsonified precipitation data for the last year in the database
A stations route that:
- [x] Returns jsonified data of all of the stations in the database

A tobs route that:
- [x] Returns jsonified data for the most active station (USC00519281)
- [x] Only returns the jsonified data for the last year of data
### API Dynamic Route
Flask application must include:

A start route that:
- [x] Accepts the start date as a parameter from the URL
- [x] Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset

A start/end route that:
- [x] Accepts the start and end dates as parameters from the URL
- [x] Returns the min, max, and average temperatures calculated from the given start date to the given end date
### Coding Conventions and Formatting
- [x] Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- [x] Name functions and variables with lowercase characters, with words separated by underscores.
- [x] Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code.
- [x] Use concise logic and creative engineering where possible.
### Deployment and Submission
- [x] Submit a link to a GitHub repository that’s cloned to your local machine and contains your files.
- [x] Use the command line to add your files to the repository.
- [x] Include appropriate commit messages in your files.
### Comments
- [x] Be well commented with concise, relevant notes that other developers can understand.
