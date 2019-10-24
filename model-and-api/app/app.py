# app/app.py# Common python package imports.
from flask import Flask, json, jsonify, request, render_template, send_file
from flask_ngrok import run_with_ngrok
import pickle
import numpy as np
import pandas as pd
import pickle
import requests
import sklearn

# Import from app/features.py.
from features import FEATURES

# Initialize the app (and set a secret_key).
app = Flask(__name__)
#app.secret_key = 'HappyHumDay'

# Run the app with ngrok
#un_with_ngrok(app)

# Load the pickled model.
MODEL = pickle.load(open('20191021_rfc_86.pkl', 'rb'))


@app.route('/')
def docs():
    """Describe the model API inputs and outputs for users."""
    return render_template('docs.html')


@app.route('/api', methods=['GET'])
def api():
    """Handle request and output model score in json format."""
    # Handle empty requests.
    if not request.json:
        return jsonify({'error': 'no request received'})    
    
    # Parse request args into feature array for prediction.
    x_list, missing_data = parse_args(request.json)
    x_array = np.array([x_list])    
    
    # Predict on x_array and return JSON response.
    estimate = int(MODEL.predict(x_array)[0])
    response = dict(ESTIMATE=estimate, MISSING_DATA=missing_data)    
    return jsonify(response)


def parse_args(request_dict):
    """Parse model features from incoming requests formatted in JSON."""
    # Initialize missing_data as False.
    missing_data = False

    # Parse out the features from the request_dict.
    x_list = []
    for feature in FEATURES:
        value = request_dict.get(feature, None)
        if value:
            x_list.append(value)
        else:
            # Handle missing features.
            x_list.append(0)
            missing_data = True
    return x_list, missing_data


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True) #for use with just Flask
    app.run() #for use with flask_ngrok 


# Run app.py in a terminal and run a request in a new terminal window:
# $ curl -X GET "http://0.0.0.0:5000/api" -H "Content-Type: application/json" --data '{"backers_count":"500", "goal":"1000", "spotlight":"0", "staff_pick":"1"}'

# Output of the terminal command above:
# {"ESTIMATE": 4, "MISSING_DATA: false"}

# Next step is setting up the application server and web server.
#  Install Gunicorn: $ pip install gunicorn 
#  Make app/wsgi.py file including the following lines of code:
# #  from app import app
# #  app.run()
#  Run the following: $ gunicorn app:app --bind 0.0.0.0:5000
#  Running the same curl command as before should yield familiar results.  

#  ngrok link for host 5000: http://9d92f013.ngrok.io 
#  Obtained by following steps on https://dashboard.ngrok.com/get-started 
#  and, importantly, spefifying the proper host for the following command:
#  $ ./ngrok http <host#> 
#  And then for running inputs through the predictive model inference the /api page like such:
#  curl -X GET "http://9d92f013.ngrok.io/api" -H "Content-Type: application/json" --data '{"backers_count":"500", "goal":"1000", "spotlight":"0", "staff_pick":"1"}'

