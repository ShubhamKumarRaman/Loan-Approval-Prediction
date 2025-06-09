# Loan Approval Prediction System

A full-stack web application to predict loan approval eligibility using a machine learning model.

## Project Structure

- `frontend/`: HTML, CSS, and JavaScript for the user interface.
- `backend/`: Flask API and ML model integration.

## Setup Instructions

### Backend

1. Install dependencies:
    ```
    cd backend
    pip install -r requirements.txt
    ```

2. Ensure `model.pkl` exists (or use the dummy model in `app.py`).

3. Run the Flask server:
    ```
    python app.py
    ```

### Frontend

1. Open `frontend/index.html` in your browser.

2. Ensure the backend is running at `http://127.0.0.1:5000`.

## Usage

- Fill out the form and click "Predict Loan Approval".
- The result will be displayed below the form.

## Notes

- For production, configure CORS and deploy the backend and frontend appropriately.
- Replace the dummy model with your trained ML model for real predictions.