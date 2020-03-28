import colorsys

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sympy import exp, arg, pi, nan
import numpy as np


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


to_plot = lambda c: c ** 2

IMAGE_W = 100
IMAGE_H = 100

image_data = [(0, 0, 0)] * IMAGE_W * IMAGE_H

if __name__ == "__main__":
    for x in range(IMAGE_W):
        for y in range(IMAGE_H):
            colour = arg(to_plot((x - IMAGE_W / 2) + (y - IMAGE_H / 2) * 1j)) / (2 * pi)
            image_data[x + y * IMAGE_W] = list(colorsys.hsv_to_rgb(float(colour) if colour != nan else 0, 0.5, 0.5))

    data = list(chunks(image_data, IMAGE_W))
    img = plt.imshow(data)
    plt.show()
