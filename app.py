import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

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
def precipitation():
    print("Server received request for 'Precipitation' page...")
    #creating session
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>= '2016-08-23')
    session.close()

    #creating a dictionary using date as the key and prcp as the value
    
    precip_dict = {} 
    for date, prcp in results:
        precip_dict[date] = prcp
    
    return jsonify(precip_dict)


if __name__ == "__main__":
    app.run(debug=True)

print("I'm done running")