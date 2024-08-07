from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the sentiment analysis model and tokenizer
model = load_model('../models/sentiment_model.h5')
with open('../models/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_sequence_length = 200  # Updated to 200

@app.route('/')
def home():
    return "Sentiment Analysis API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    if not text:
        return jsonify({'error': 'Please enter text for prediction.'}), 400

    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
    prediction = model.predict(padded_sequences)[0][0]

    sentiment = 'Positive' if prediction >= 0.5 else 'Negative'  # Adjusting threshold to 0.5

    return jsonify({'text': text, 'prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
