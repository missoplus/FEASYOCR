import difflib

def correct_spelling(text, reference_list):
    """
    اصلاح متن استخراج‌شده با استفاده از نزدیک‌ترین تطابق به لیست اسامی Ground Truth.
    """
    words = text.strip().split()
    corrected_words = []

    for word in words:
        match = difflib.get_close_matches(word, reference_list, n=1, cutoff=0.6)
        corrected_words.append(match[0] if match else word)

    return " ".join(corrected_words)
