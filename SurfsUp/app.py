import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Convert the query results from your precipitation analysis
    # (i.e. retrieve only the last 12 months of data) to a 
    # dictionary using date as the key and prcp as the value.
    annual_prcp = session.query(Measurement.date, Measurement.prcp).\
                  filter(Measurement.date >= '2016-08-23').all()

    session.close()

    all_prcp = []
    for date, prcp in annual_prcp:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)

    # Return the JSON representation of your dictionary.
    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    stations = session.query(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(stations)
    # Return jsonified data of all of the stations in the database
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all tobs"""
    # Only returns the jsonified data for the last year of data
    temp_obs = session.query(Measurement.tobs).\
                  filter(Measurement.station == 'USC00519281').\
                  filter(Measurement.date >= '2016-08-23').all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(temp_obs)
    # Return jsonified data for the most active station (USC00519281)
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def tobs_since(start: dt.date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates
    # greater than or equal to the start date
    stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                  filter(Measurement.date >= start).first()
                #   filter(Measurement.station == 'USC00519281').\

    session.close()

    # Return a JSON list of the minimum temperature, the average temperature,
    # and the maximum temperature for a specified start
    return jsonify({'min': stats[0], 'max': stats[1], 'avg': stats[2]})


@app.route("/api/v1.0/<start>/<end>")
def tobs_between(start: dt.date, end: dt.date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # For a specified start date and end date, calculate TMIN, TAVG, 
    # and TMAX for the dates from the start date to the end date, inclusive
    stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                  filter(Measurement.date >= start).\
                  filter(Measurement.date <= end).\
                  first()
                #   filter(Measurement.station == 'USC00519281').\

    session.close()

    # Return a JSON list of the minimum temperature, the average temperature,
    # and the maximum temperature for a specified start
    return jsonify({'min': stats[0], 'max': stats[1], 'avg': stats[2]})


if __name__ == '__main__':
    app.run(debug=True)