import tkinter as tk
from PIL import Image, ImageDraw

from image_preprocessing import preprocess_drawn_image
from predict import predict_digit

CANVAS_SIZE = 280

root = tk.Tk()
root.title("Handwritten Digit Spot Detection")

canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black")
canvas.grid(row=0, column=0, columnspan=2)

image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), "black")
draw = ImageDraw.Draw(image)

last_x, last_y = None, None


def draw_digit(event):
    global last_x, last_y
    x, y = event.x, event.y
    if last_x:
        canvas.create_line(last_x, last_y, x, y,
                           width=20, fill="white", capstyle=tk.ROUND)
        draw.line([last_x, last_y, x, y], fill="white", width=20)
    last_x, last_y = x, y


def reset(event):
    global last_x, last_y
    last_x, last_y = None, None


def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, CANVAS_SIZE, CANVAS_SIZE], fill="black")
    result_label.config(text="Prediction: ")


def predict():
    processed = preprocess_drawn_image(image)
    if processed is None:
        result_label.config(text="Prediction: Draw something!")
        return

    digit, confidence = predict_digit(processed)
    result_label.config(text=f"Prediction: {digit} ({confidence:.1f}%)")


canvas.bind("<B1-Motion>", draw_digit)
canvas.bind("<ButtonRelease-1>", reset)

tk.Button(root, text="Predict", command=predict, width=15).grid(row=1, column=0)
tk.Button(root, text="Clear", command=clear_canvas, width=15).grid(row=1, column=1)

result_label = tk.Label(root, text="Prediction: ", font=("Arial", 16))
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
