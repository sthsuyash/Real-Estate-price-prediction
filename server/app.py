from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


# post request to predict the price
@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    # jsonify converts the response to json format
    response = jsonify({
        'estimated_price': utils.get_estimated_price(total_sqft, bath, bhk)
        # get_estimated_price is a function from utils.py
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # to allow cross origin resource sharing

    return response


if __name__ == '__main__':
    app.run(port=8000)
