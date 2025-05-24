import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # حذف نویز نرم
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return image