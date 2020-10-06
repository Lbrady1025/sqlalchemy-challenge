import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement

station = Base.classes.station

app = Flask(__name__)

@app.route('/')
def welcome():
    return(f"Welcome to the Hawaii Weather API!</br>"
        f"Available routes: </br>"
        f"/api/v1.0/precipitation </br>"
        f"/api/v1.0/stations </br>"
        f"/api/v1.0/tobs </br>"
        f"/api/v1.0/<start> </br>"
        f"/api/v1.0/<start>/<end> </br>")

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

    results = session.query(station.name).group_by(station.station)

    session.close()

    all_stations = []

    for name in results:
        stations_dict = {}
        stations_dict['name'] = name
        all_stations.append(stations_dict)
    
    return jsonify(all_stations)

@app.route('/api/v1.0/tobs')
def temps():

    session = Session(engine)

    session.query(measurement.date).order_by(measurement.date.desc()).first()
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(measurement.date,measurement.prcp).\
        filter(measurement.date >= year_ago).\
        filter(measurement.station == 'USC00519281').all()

    session.close()

    all_year_temps = []

    for date,prcp in results:
        temp_dict = {}
        temp_dict['date'] = date
        temp_dict['prcp'] = prcp
        all_year_temps.append(temp_dict)
    
    return jsonify(all_year_temps)

@app.route('/api/v1.0/<start>')
def start(start):
    
    session = Session(engine)
    
    results = session.query(measurement.date)
    
    start_date = date.replace(" ", "")
    for date in results:
        search_term = results["date"].replace(" ", "")

        temp_min = session.query(func.min(measurement.tobs)).\
            filter(measurement.date >= search_term).all()
        temp_max = session.query(func.max(measurement.tobs)).\
            filter(measurement.date >= search_term).all()
        temp_avg = session.query(func.avg(measurement.tobs)).\
            filter(measurement.date >= search_term).all()

        if search_term == start_date:        
            return jsonify(date)

    return jsonify({"error": "Date not found."}), 404


# if __name__ == '__main__':
#     app.run(debug=True)