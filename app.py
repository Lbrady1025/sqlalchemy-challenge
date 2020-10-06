import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route('/')
def welcome():
    return(f"Welcome to the Hawaii Weather API!</br>"
        f"Available routes: </br>")

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    
    results = session.query(measurement.date,measurement.prcp).all()
    
    session.close()

    all_precip = []

    for date,prcp in results:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['prcp'] = prcp
        all_precip.append(precip_dict)
    
    return jsonify(all_precip)

@app.route('/api/v1.0/stations')
def stations():

    session = Session(engine)

    results = session.query(measurement.station).group_by(measurement.station)

    all_stations = []

    for station in results:
        stations_dict = {}
        stations_dict['station'] = station
        all_stations.append(stations_dict)
    
    return jsonify(all_stations)

# @app.route('/api/v1.0/tobs')
# def temps():



if __name__ == '__main__':
    app.run(debug=True)