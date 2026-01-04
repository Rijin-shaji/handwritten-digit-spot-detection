import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "../models/model.h5"

model = load_model(MODEL_PATH)


def predict_digit(processed_image):
    """
    Takes preprocessed image and returns digit and confidence.
    """
    prediction = model.predict(processed_image, verbose=0)
    digit = np.argmax(prediction)
    confidence = prediction[0][digit] * 100
    return digit, confidence
