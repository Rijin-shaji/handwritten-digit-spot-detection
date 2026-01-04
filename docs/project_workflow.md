Project Workflow

This project implements an end-to-end handwritten digit recognition system using a deep learning model and a graphical user interface.

Workflow Steps

User draws a handwritten digit on the Tkinter canvas

The drawn image is captured in grayscale format

Image preprocessing is applied:

Noise removal

Digit cropping using bounding box detection

Resizing while preserving aspect ratio

Centering on a 28×28 canvas

Normalization (pixel values scaled to 0–1)

Preprocessed image is passed to the trained CNN model

Model predicts the digit (0–9) with confidence score

Prediction result is displayed in the GUI

Output

Predicted digit

Confidence percentage
