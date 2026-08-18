print("Enter file name: ")
filename = input()

try:
    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()

except FileNotFoundError:
    print(f"File {filename} does not exist!")

else:
    print(f"File {filename} read successfully!")
    text = file_content.split()
    print(f"File {filename} contains {len(text)} words")

    