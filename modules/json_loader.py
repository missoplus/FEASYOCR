import json

def load_ground_truth(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # خروجی: {'78861576.jpg': ['AABJÖE REINHARD'], ...}
    ground_truth = {}
    for image_id, people in data.items():
        names = [f"{person['Name']} {person['Vorname']}" for person in people]
        ground_truth[f"{image_id}.jpg"] = names
    return ground_truth
