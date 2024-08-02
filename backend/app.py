# Backend app

from flask import Flask, request, jsonify
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pandas as pd

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('../models/sentiment_model.h5')

# Prepare the tokenizer
train_data = pd.read_csv('../data/processed/train_data.csv')
max_words = 5000
max_len = 200
tokenizer = Tokenizer(num_words=max_words, lower=True)
tokenizer.fit_on_texts(train_data['review'].values)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data['review']
    
    # Preprocess the review
    seq = tokenizer.texts_to_sequences([review])
    padded = pad_sequences(seq, maxlen=max_len)
    
    # Predict sentiment
    pred = model.predict(padded)
    sentiment = 'positive' if np.argmax(pred) == 1 else 'negative'
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
