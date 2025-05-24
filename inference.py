import os
import csv
import cv2
from modules.json_loader import load_ground_truth
from modules.ocr_easyocr import extract_text
from modules.evaluator import calculate_accuracy
from modules.preprocessor import preprocess_image
from modules.spellcorrect import correct_spelling

# مسیرها
dataset_path = "CM1-Dataset"
json_path = "data/personen.json"
ground_truth = load_ground_truth(json_path)

# ایجاد فایل خروجی
with open("results.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Image", "Extracted Text", "Ground Truth", "Accuracy"])
    # آماده‌سازی لیست اسامی برای تصحیح املا
    reference_names = []
    for entries in ground_truth.values():
        for full_name in entries:
            reference_names.extend(full_name.lower().split())

    for image_name in os.listdir(dataset_path):
        if not image_name.endswith(".jpg"):
            continue

        image_path = os.path.join(dataset_path, image_name)

        # پیش‌پردازش تصویر
        preprocessed_image = preprocess_image(image_path)
        temp_path = "temp.jpg"
        cv2.imwrite(temp_path, preprocessed_image)

        # استخراج متن
        extracted = extract_text(temp_path)

        # مقایسه با Ground Truth
        expected = ground_truth.get(image_name, [])
        accuracy = calculate_accuracy(extracted, expected)

        # چاپ و ذخیره
        print(f"\n🖼️ Image: {image_name}")
        print(f"🔍 Extracted: {extracted}")
        print(f"✅ Ground Truth: {expected}")
        print(f"📊 Accuracy: {accuracy}%")

        writer.writerow([image_name, extracted, "; ".join(expected), accuracy])
