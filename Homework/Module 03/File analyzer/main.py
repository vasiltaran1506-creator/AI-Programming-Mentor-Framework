from filesystem import find_txt_files
from analyzer import count_words_in_files
from pathlib import Path


def main():
    total_words = []
    
    folder_path = Path(input("Enter folder path: "))
    if folder_path.exists():
        if folder_path.is_dir():
            files_list = find_txt_files(folder_path)
        elif folder_path.is_file():
            print(f"Path {folder_path} is file path. Enter folder path")
            return
        else: 
            print("Unexpected error")
            return
    else:
        print("Unexpected error")
        return

    for file in files_list:
        words_in_file = count_words_in_files(file)
        total_words.append(words_in_file)
        print(f"In file '{file.name}' is {words_in_file} words.")

    print(f"Total words in all files: {sum(total_words)}")

if __name__ == "__main__":
    main()
