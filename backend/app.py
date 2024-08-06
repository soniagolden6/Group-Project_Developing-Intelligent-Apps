from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Load the sentiment analysis model and tokenizer
model = load_model('../models/sentiment_model.h5')
with open('../models/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_sequence_length = 200  # Updated to 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('index.html', error='Please enter text for prediction.')
        
        sequences = tokenizer.texts_to_sequences([text])
        padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
        prediction = model.predict(padded_sequences)[0][0]

        sentiment = 'Positive' if prediction <= 0.5 else 'Negative'  # Adjusting threshold to 0.5

        return render_template('index.html', text=text, prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
