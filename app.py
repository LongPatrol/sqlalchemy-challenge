from flask import Flask, jsonify

app = Flask(__name__)

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
if __name__ == "__main__":
    app.run(debug=True)
print("I'm done running")