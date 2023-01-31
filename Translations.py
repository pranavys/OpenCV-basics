import cv2
import numpy as np
from matplotlib import pyplot as plt


def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('images/1.jpg')
imshow("Original", image)

height, width = image.shape[:2]
quarter_height, quarter_width = height/4, width/4
T = np.float32([[1, 0, quarter_width], [0, 1,quarter_height]])
img_translation = cv2.warpAffine(image, T, (width, height))
imshow("Translated", img_translation)