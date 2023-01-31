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

image = cv2.imread('images/2.jpg')
imshow("Original", image)
height, width = image.shape[:2]


rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)


rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
imshow("Rotated 90 degrees with scale = 1", rotated_image)