import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

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


@app.route('/api/v1.0/stations')
def stations():


@app.route('/api/v1.0/tobs')
def temps():