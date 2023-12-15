# Vehicle Maintenance Prediction

## Overview

This project aims to predict engine maintenance requirements based on various engine parameters. It utilizes a Random Forest classifier trained on a dataset containing features such as Engine RPM, Lub Oil Pressure, Fuel Pressure, Coolant Pressure, Lub Oil Temperature, and Coolant Temperature.

## Project Structure

- **`train.py`**: Script to train the Random Forest model on the provided dataset.
- **`app.py`**: Flask application for deploying the trained model and providing a user interface.
- **`index.html`**: HTML template for the user interface.
- **`trained_model.joblib`**: Serialized trained model file.
- **`your_dataset.csv`**: Sample dataset file (replace with your actual dataset).
- **`static/`**: Directory for static files like CSS.
- **`templates/`**: Directory for Flask HTML templates.
- **`reports/`**: Directory for project reports.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harishvarma0717/ADM_Project_Final.git
   cd ADM_Project_Final
2. Install Dependencies:

pip install -r requirements.txt

3. Train the Model:

python train.py

4. Run the Flask App:

python app.py

5. Access the Application:

Open your web browser and go to http://127.0.0.1:5000/


Usage

Enter engine parameters in the form on the web interface.
Click "Predict" to get maintenance predictions.

Project Details:

Problem Definition: Predicting engine maintenance requirements.

Data Preprocessing: Handling missing values, outliers, and ensuring data quality.

Feature Engineering: Creating new features like RPM_Difference and Lub_Oil_Pressure_Rolling_Avg.

Model Development: Using a Random Forest classifier.

Evaluation: Metrics include accuracy, precision, recall, and the ROC curve.

Deployment: The trained model is deployed using Flask.


Dependencies:
Flask
scikit-learn
pandas
matplotlib
