from pathlib import Path

def find_txt_files(folder_path):
    path = Path(folder_path)
    files_list = list(path.glob("*.txt"))
    return files_list

if __name__ == "__main__":
    print("Running test")



        