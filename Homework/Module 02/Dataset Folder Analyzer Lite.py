from pathlib import Path

def read_folder(folder_path):
    folder = Path(folder_path)
    if folder.exists() and folder.is_dir():
        files_list = []
        for file in folder.iterdir():
            if file.is_file(): 
                with open(file, "r", encoding="utf-8") as text_file:
                    for line in text_file:
                        clean_line = line.strip()
                        file_name, file_ext = clean_line.rsplit(".", 1)
                        file_ext = "." + file_ext
                file_data = {
                    "name": file_name,
                    "extention": file_ext,
                    "name_length": len(file_name),
                    "full_name": clean_line
                }
                files_list.append(file_data)
    else:
        print("No folder found")


def main():
    folder_path = input("Enter folder path: ")
    files_list = read_folder(folder_path)
    print(files_list)
    return 

main()
