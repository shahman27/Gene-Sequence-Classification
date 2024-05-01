import os

def get_file_names(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Adds the file name to the list
            file_names.append(os.path.join(root, file))
    return file_names


