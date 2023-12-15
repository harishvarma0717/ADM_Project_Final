from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        input_values = [
            float(input_data['Engine_RPM']),
            float(input_data['Lub_Oil_Pressure']),
            float(input_data['Fuel_Pressure']),
            float(input_data['Coolant_Pressure']),
            float(input_data['Lub_Oil_Temp']),
            float(input_data['Coolant_Temp']),
        ]

        prediction = model.predict([input_values])[0]

        maintenance_required = bool(prediction)  # Convert prediction to a boolean value

        return jsonify({'maintenance_required': maintenance_required})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
