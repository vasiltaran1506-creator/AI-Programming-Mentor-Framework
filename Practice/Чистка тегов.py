raw_tags = input("Enter tags:")

def clear_tags(text_to_clean):
    clean_tags = []
    cleaned_text = text_to_clean.strip()
    word_list = cleaned_text.split(",")
    for word in word_list:
        word = word.strip().lower()
        clean_tags.append(word)
    return clean_tags

result = clear_tags(raw_tags)

print(f"List of clean tags: {result}")

