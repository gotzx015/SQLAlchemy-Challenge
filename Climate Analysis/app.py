# Import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt
from flask import Flask, jsonify

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Climate Data API! <br/>"
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start_date> <br/>"
        "Enter start date in this format: /api/v1.0/2015-08-23 <br/>"
        f"/api/v1.0/<start_date>/<end_date> <br/>"
        "Enter start and end date in this format: /api/v1.0/2015-08-23/2016-08-23"
    )



@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)

    results = session.query(measurement.date, func.max(measurement.prcp))\
    .group_by(measurement.date)\
    .all()

    session.close()

    prcp_data = list(np.ravel(results))

    return jsonify(prcp_data)



@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(measurement.station).distinct().all()

    session.close()

    stations = list(np.ravel(results))

    return jsonify(stations)



@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(measurement.date, measurement.tobs)\
    .filter(measurement.date >= query_date)\
    .filter(measurement.station == "USC00519281")\
    .all()

    session.close()

    temp = list(np.ravel(results))

    return jsonify(temp)



@app.route("/api/v1.0/<start_date>")
def start(start_date):
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs))\
    .filter(measurement.date >= start_date)\
    .all()

    session.close()

    temp = list(np.ravel(results))

    return jsonify(temp)



@app.route("/api/v1.0/<start_date>/<end_date>")
def end(start_date, end_date):
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs))\
    .filter(measurement.date >= start_date)\
    .filter(measurement.date <= end_date)\
    .all()

    session.close()

    temp = list(np.ravel(results))

    return jsonify(temp)

if __name__ == "__main__":
    app.run(debug=True)
