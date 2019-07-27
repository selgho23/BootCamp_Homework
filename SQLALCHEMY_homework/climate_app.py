# Dependencies
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

######################
### DATABASE SETUP ###
######################

engine = engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Start and end date of the last year data was acquired
last_day = dt.date(2017, 8, 23)
twelve_months_ago = last_day - relativedelta(months=12)

###################
### FLASK SETUP ###
###################
app = Flask(__name__)

####################
### FLASK ROUTES ###
####################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Returns precipitation data over the last year."""
    session = Session(engine)

    # Collect precipitation data
    sel = sel = [Measurement.date, Measurement.prcp]
    results = session.query(*sel).\
              filter(Measurement.date <= last_day).\
              filter(Measurement.date >= twelve_months_ago).\
              order_by(Measurement.date.desc()).all()

    # Convert results to a dictionary with 'date' as the key and 
    # 'precipitation' as the value
    key_value = ['Date', 'Precipitation']
    precipitation_dict = [dict(zip(key_value, row))
                          for row in results]
 
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Returns a list of obervation stations."""
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()

    # Convert list of tuples to list
    stations = list(np.ravel(results)) 
    
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Returns temperature observation data over the last year."""
    session = Session(engine)

    # Collect tobs data
    sel = [Measurement.date, Measurement.tobs]
    results = session.query(*sel).\
              filter(Measurement.station == 'USC00519281').\
              filter(Measurement.date <= last_day).\
              filter(Measurement.date >= twelve_months_ago).\
              order_by(Measurement.date.desc()).all()

    # Convert results to a dictionary with 'date' as the key and 
    # 'temperature data' as the value
    key_value = ['Date', 'Temperature Data']
    tempObs_dict = [dict(zip(key_value, row))
                    for row in results]

    return jsonify(tempObs_dict)

@app.route("/api/v1.0/<start>")
def tobs_stats_start(start):
    """Returns a list of the minimum, average, and maximum
       temperatures for the range of dates greater than the
       start date."""
    session = Session(engine)

    # Query
    sel = [func.min(Measurement.tobs), 
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).all()

    # Convert list of tuples to list
    temp_stats = list(np.ravel(results))

    # Round every element in temp_stats to the two significant figures
    temp_stats = [round(temp, 2) for temp in temp_stats]

    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def tobs_stats_start_end(start,end):
    """Returns a list of the minimum, average, and maximum
       temperatures for the range of dates between the
       start date and the end date."""
    session = Session(engine)

    # Query
    sel = [func.min(Measurement.tobs), 
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).\
              filter(Measurement.date <= end).all()

    # Convert list of tuples to list
    temp_stats = list(np.ravel(results))

    # Round every element in temp_stats to the two significant figures
    temp_stats = [round(temp, 2) for temp in temp_stats]

    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run()