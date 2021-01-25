import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import pandas as pd

#Database setup
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#Flask setup
app = Flask(__name__)

#Flask routes
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return(
        f'Available routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/[start date]<br/>'
        f'/api/v1.0/[start date]/[end date]'
    )

@app.route("/api/v1.0/precipitation")
def precipitation_func():
    print("Server received request for 'Precipitation' page...")
    #creating session
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>= '2016-08-23')
    session.close()

    #creating a dictionary using date as the key and prcp as the value
    
    precip_dict = {} 
    for (date, prcp) in results:
         #Trying to find a way to print all of the precipitation observations for a particular day, but it's still not working.
        prcp_list = []

        if pd.isnull(prcp) == False:
            prcp_list.append(prcp)
        else:
            prcp_list.append(prcp)
      
        precip_dict[date] = prcp_list    

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station)
    session.close()

    station_list = []
    for result in results:
        station_list.append(result)

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.station == 'USC00519281', Measurement.date>= '2016-08-23')
    session.close()

    temperature_list = []
    for result in results:
        temperature_list.append(result)

    return jsonify(temperature_list)

@app.route("/api/v1.0/<string:start>")
def start_only(start):
    session = Session(engine)
    results = session.query(func.tmin(Measurement.tobs), func.tmax(Measurement.tobs), func.tavg(Measurement.tobs)).filter(Measurement.date >= start)
    session.close()

    start_list = []
    for result in results:
        start_list.append(result)

    return jsonify(start_list)

if __name__ == "__main__":
    app.run(debug=True)


print("I'm done running")