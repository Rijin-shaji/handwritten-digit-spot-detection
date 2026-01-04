import numpy as np
from PIL import Image


def preprocess_drawn_image(image, canvas_size=280):
    """
    Crops, resizes, centers, and normalizes the drawn digit
    to 28x28 format required by CNN.
    """

    img_array = np.array(image)

    rows = np.any(img_array > 0, axis=1)
    cols = np.any(img_array > 0, axis=0)

    if not rows.any() or not cols.any():
        return None

    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    padding = 20
    rmin = max(0, rmin - padding)
    rmax = min(canvas_size, rmax + padding)
    cmin = max(0, cmin - padding)
    cmax = min(canvas_size, cmax + padding)

    cropped = img_array[rmin:rmax, cmin:cmax]
    img_pil = Image.fromarray(cropped)

    width, height = img_pil.size
    if width > height:
        new_width = 20
        new_height = int(20 * height / width)
    else:
        new_height = 20
        new_width = int(20 * width / height)

    resized = img_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)

    final_img = Image.new("L", (28, 28), 0)
    offset_x = (28 - new_width) // 2
    offset_y = (28 - new_height) // 2
    final_img.paste(resized, (offset_x, offset_y))

    final_array = np.array(final_img) / 255.0
    return final_array.reshape(1, 28, 28, 1)
