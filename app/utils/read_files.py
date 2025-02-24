import os


def read_files(directory_path) -> dict:
    contents = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                contents[file] = content
    return contents
