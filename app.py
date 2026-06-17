import streamlit as st
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
from PIL import Image
import os

# Use existing variables: model, tokenizer, vgg_model, max_length, features, mapping

st.title("Image Captioning App")

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def predict_caption(model, image, tokenizer, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
        yhat = model.predict([image, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idx_to_word(yhat, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    return in_text

vgg_model = VGG16()
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

MODEL_PATH = "working/best_model.h5"
model = load_model(MODEL_PATH)

FEATURES_PATH = "working/features.pkl"
with open(FEATURES_PATH, 'rb') as f:
    tokenizer = pickle.load(f)

max_length = 34  # Replace with the actual max length from your training

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    img = image.resize((224, 224))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    feature = vgg_model.predict(img, verbose=0)
    caption = predict_caption(model, feature, tokenizer, max_length)
    st.write("*Generated Caption:*")
    st.write(caption)