from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

# Try to load a real model, else use a dummy model
try:
    model = joblib.load('model.pkl')
except Exception:
    class DummyModel:
        def predict(self, X):
            # Approve if applicant income > 5000, else not approved
            return [1 if x[4] > 5000 else 0 for x in X]
    model = DummyModel()

def preprocess(data):
    gender = 1 if data.get('gender') == 'Male' else 0
    married = 1 if data.get('married') == 'Yes' else 0
    dependents = 3 if data.get('dependents') == '3+' else int(data.get('dependents', 0))
    education = 1 if data.get('education') == 'Graduate' else 0
    self_employed = 1 if data.get('self_employed') == 'Yes' else 0
    applicant_income = float(data.get('applicant_income', 0))
    coapplicant_income = float(data.get('coapplicant_income', 0))
    loan_amount = float(data.get('loan_amount', 0))
    loan_amount_term = float(data.get('loan_amount_term', 360))
    credit_history = int(data.get('credit_history', 1))
    property_area = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}.get(data.get('property_area'), 1)
    return [[gender, married, dependents, education, applicant_income, coapplicant_income,
             loan_amount, loan_amount_term, credit_history, self_employed, property_area]]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        features = preprocess(input_data)
        prediction = model.predict(features)[0]
        result = "Approved" if prediction == 1 else "Not Approved"
        return jsonify({'loan_status': result})
    except Exception as e:
        return jsonify({'error': 'Prediction failed', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)