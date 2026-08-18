def count_words_in_files(file):
    with open(file, "r", encoding="utf-8") as single_file:
        text = single_file.read()
        words = text.split()
        words_in_file = len(words)
    return words_in_file

if __name__ == "__main__":
    print("Running test")


