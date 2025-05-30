

import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet50
from PIL import Image
import numpy as np
from torchvision.models.segmentation import deeplabv3_resnet50, DeepLabV3_ResNet50_Weights
import cv2

weights = DeepLabV3_ResNet50_Weights.DEFAULT
model = deeplabv3_resnet50(weights=weights)
model.eval()

transform = T.Compose([
    T.Resize((256, 256)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predict_rooftop_area(image_array):
   
    gray = np.mean(image_array, axis=2)
    mask = (gray > 0.4).astype(np.uint8)
    kernel = np.ones((3, 3), np.uint8)
    cleaned_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return cleaned_mask.astype(bool)

def calculate_confidence(mask):
    total_pixels = mask.size
    positive_pixels = mask.sum()
    ratio = positive_pixels / total_pixels
    if ratio < 0.01:
        return "Low confidence"
    elif ratio < 0.1:
        return "Moderate confidence"
    else:
        return "High confidence"
