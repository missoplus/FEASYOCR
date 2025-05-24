import easyocr

reader = easyocr.Reader(['de', 'en'])

def extract_text(image_path):
    results = reader.readtext(image_path, detail=0)
    return " ".join(results)
