# Import the dependencies.

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with = engine)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

Session = session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__app__)

#################################################
# Flask Routes
#################################################

     #app.route("/")

#Start at the homepage.
#List all the available routes.

     #app.route("/api/v1.0/precipitation")

#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as #the key and prcp as the value.
#Return the JSON representation of your dictionary.

     #app.route("/api/v1.0/stations")

#Return a JSON list of stations from the dataset.

     #app.route("/api/v1.0/tobs")

#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.

     #app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end #range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


if __name__ == "__main__":
    app.run(debug=True)