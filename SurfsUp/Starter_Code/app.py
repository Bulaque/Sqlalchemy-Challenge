
#       URL is html://127.0.0.1:5000

# Import the dependencies.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with = engine)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

Session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    return (f"Available routes: "
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/<start> and /api/v1.0/<start>/<end>")

# Start at the homepage
# List all the available routes

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Query from Precipitation Analysis
    
    Timerange = Session.query(Measurement.date, Measurement.prcp).all()
    Timerange1 = [{"date": row.date, "prcp": row.prcp} for row in Timerange]
    
    return jsonify(Timerange1)


    
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as #the key and prcp as the value.
#Return the JSON representation of your dictionary.

@app.route("/api/v1.0/stations")
def stations():
    
    # Query list of stations
    Station_amount = Session.query(Station.station).all()
    stations_list = [dict(row) for row in Station_amount]
    
    return jsonify(stations_list)


#Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/tobs")
def Most_Active():
    
    # Query dates and temperature  
    Active = Session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').all()
    Active_list = [dict(row) for row in Active]

    return jsonify(Active_list)

    
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/<start>")
def Temp_Range_Beginning():

    # Query min, max, and avg temperature from a start point
    First_date = '2016-06-01'
    Beginning = Session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date > First_date).order_by(Measurement.date.desc()).all()
    Beginning_list = [dict(row) for row in Beginning]

    return jsonify(Beginning_list)

@app.route("/api/v1.0/<start>/<end>")
def Temp_Range():

    # Query min, max, and avg temperature from a start to an end point
    First_date = '2016-06-01'
    Last_date = '2017-10-04'
    Start_to_End = Session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date.between(First_date, Last_date)).order_by(Measurement.date.desc()).all()
    Start_to_end_list = [dict(row) for row in Start_to_End]

    return jsonify(Start_to_end_list)

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end #range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


if __name__ == "__main__":
    app.run(debug=True)