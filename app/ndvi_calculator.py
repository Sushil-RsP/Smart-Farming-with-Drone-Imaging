
import numpy as np
import cv2

def preprocess_image(image, size=(256, 256)):
    resized = cv2.resize(image, size)
    normalized = resized / 255.0
    return normalized

def calculate_ndvi(nir_channel, red_channel):
    nir = nir_channel.astype(float)
    red = red_channel.astype(float)
    ndvi = (nir - red) / (nir + red + 1e-6)
    return ndvi

def load_image(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    return img
