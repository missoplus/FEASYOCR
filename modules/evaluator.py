def calculate_accuracy(predicted, ground_truth_list):
    predicted_words = set(predicted.lower().split())

    max_score = 0
    for true_label in ground_truth_list:
        gt_words = set(true_label.lower().split())
        match_count = len(predicted_words & gt_words)
        score = (match_count / len(gt_words)) * 100 if gt_words else 0
        max_score = max(max_score, score)

    return round(max_score, 2)
