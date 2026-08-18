from pathlib import Path

text_path = input("Enter file path: ")
filepath = Path(text_path)

if filepath.is_dir():
    print(f"All .txt files in {filepath}: ")
    files = list(filepath.glob("*.txt"))

    print(f"Files in {filepath}:\n")
    for N, file in enumerate(files):
        print(f"{N + 1}. {file.name}")

    print(f"Total files in {filepath}: {len(files)}") 

elif filepath.is_file():
    print(f"{filepath} is not directory, it is file")
else: 
    print(f"Path {filepath} does not existing")