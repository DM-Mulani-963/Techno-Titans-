from flask import Flask, request, jsonify
from flask_cors import CORS
from models.disease_prediction import predict_disease
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        user_id = data.get('userId')
        
        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400
        
        # Get prediction from model
        prediction = predict_disease(symptoms)
        
        # Store prediction in Firestore
        if user_id:
            prediction_ref = db.collection('predictions').document()
            prediction_ref.set({
                'userId': user_id,
                'symptoms': symptoms,
                'prediction': prediction,
                'timestamp': firestore.SERVER_TIMESTAMP
            })
        
        return jsonify(prediction)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    from models.disease_prediction import symptoms
    return jsonify({'symptoms': symptoms})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 