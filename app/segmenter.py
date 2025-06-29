
import numpy as np

def dummy_unet_segmentation(ndvi):
    # <0.2 = stressed, 0.2-0.5 = moderate, >0.5 = healthy
    segmented = np.zeros_like(ndvi)
    segmented[ndvi > 0.5] = 2
    segmented[(ndvi > 0.2) & (ndvi <= 0.5)] = 1
    segmented[ndvi <= 0.2] = 0
    return segmented
