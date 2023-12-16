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

## Usage
The usage of this application is designed to be straightforward for users:

### Enter engine parameters: On the web interface, users can input engine parameters such as Engine RPM, Lub Oil Pressure, Fuel Pressure, Coolant Pressure, Lub Oil Temperature, and Coolant Temperature.

### Predict maintenance: After entering the parameters, users can click the "Predict" button. The application will use the trained Random Forest model to provide predictions on whether the engine requires maintenance.

## Project Details
### Problem Definition
The primary objective of this project is to predict engine maintenance requirements. By analyzing the input parameters, the model determines whether a vehicle engine is likely to need maintenance.

### Data Preprocessing
Data preprocessing is a critical step to ensure the quality of the input data. This involves handling missing values, identifying and managing outliers, and ensuring overall data cleanliness. Robust preprocessing contributes to the accuracy and reliability of the predictive model.

### Feature Engineering
Feature engineering involves creating new features or modifying existing ones to enhance the model's predictive capabilities. In this project, additional features such as RPM_Difference and Lub_Oil_Pressure_Rolling_Avg are engineered to provide more meaningful information to the model.

### Model Development
The core of the project lies in developing a predictive model. A Random Forest classifier is employed for this task. Random Forest is chosen for its ability to handle complex relationships in data and provide accurate predictions.

### Evaluation
The model's performance is evaluated using various metrics, including accuracy, precision, recall, and the Receiver Operating Characteristic (ROC) curve. These metrics help gauge the model's effectiveness and identify areas for potential improvement.

### Deployment
The trained Random Forest model is deployed using Flask, a web framework for Python. Flask allows for the creation of a user-friendly web interface, enabling users to interact with the model and receive predictions conveniently.

These details provide a comprehensive overview of the project's objectives, methodologies, and the user experience.


## Dependencies:
Flask
scikit-learn
pandas
matplotlib
