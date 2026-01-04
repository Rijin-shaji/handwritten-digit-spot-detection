System Architecture

This system follows a modular architecture separating user interface, preprocessing, and model inference.

System Components

User Interface (Tkinter GUI)
Allows users to draw handwritten digits

Image Preprocessing Module
Handles cropping, resizing, centering, and normalization

Prediction Module
Loads the trained CNN model and performs inference

Output Module
Displays predicted digit and confidence score

Data Flow

User Input → GUI → Image Preprocessing → CNN Model → Prediction Output
