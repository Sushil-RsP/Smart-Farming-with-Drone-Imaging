
import matplotlib.pyplot as plt
import numpy as np
import cv2

def show_ndvi(ndvi):
    plt.figure(figsize=(6, 5))
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title("NDVI Heatmap")
    plt.axis('off')
    plt.show()

def show_segmentation(segmented):
    plt.figure(figsize=(6, 5))
    plt.imshow(segmented, cmap='Accent')
    plt.title("Segmented Vegetation Classes")
    plt.axis('off')
    plt.show()

def overlay_segmentation(image, mask):
    overlay = image.copy()
    overlay[mask == 0] = [0, 0, 255]    # Red for stressed
    overlay[mask == 1] = [0, 255, 255]  # Yellow for moderate
    overlay[mask == 2] = [0, 255, 0]    # Green for healthy
    return overlay

def show_overlay(image, mask):
    overlaid = overlay_segmentation(image, mask)
    plt.figure(figsize=(6, 5))
    plt.imshow(cv2.cvtColor(overlaid, cv2.COLOR_BGR2RGB))
    plt.title("Overlay: Image + Segmentation")
    plt.axis('off')
    plt.show()

def compute_field_statistics(ndvi, segmented):
    total_pixels = ndvi.size
    healthy = np.sum(segmented == 2)
    moderate = np.sum(segmented == 1)
    stressed = np.sum(segmented == 0)
    return {
        "Healthy (%)": round((healthy / total_pixels) * 100, 2),
        "Moderate (%)": round((moderate / total_pixels) * 100, 2),
        "Stressed (%)": round((stressed / total_pixels) * 100, 2),
        "Mean NDVI": round(float(np.mean(ndvi)), 3)
    }
