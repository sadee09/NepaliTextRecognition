from flask import Flask, render_template, url_for, request, redirect
import json 
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

import random
import pickle

DATA_PATH = '/Users/sauravshrestha/Documents/chatbot/updated_response_data.json'

with open(DATA_PATH) as file:
    RESPONSE = json.load(file)

MODEL = tf.keras.models.load_model('/Users/sauravshrestha/Documents/chatbot/chat_model_final')

with open('/Users/sauravshrestha/Documents/chatbot/tokenizer_final.pickle', 'rb') as handle:
    TOKENIZER = pickle.load(handle)

with open('/Users/sauravshrestha/Documents/chatbot/label_encoder_final.pickle', 'rb') as enc:
        LABEL_ENCODER = pickle.load(enc)

MAX_LEN = 20


def get_response(user_inp):
    result = MODEL.predict(tf.keras.preprocessing.sequence.pad_sequences(TOKENIZER.texts_to_sequences([user_inp]),
                                             truncating='post', maxlen=MAX_LEN), verbose=0)
    
    if np.max(result) > 0.7:
        tag = LABEL_ENCODER.inverse_transform([np.argmax(result)])
    else:
        tag = ['error']

    print(tag)
    return RESPONSE[tag[0]]



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return get_response(userText)


if __name__ == '__main__':
    app.run(port=5000)