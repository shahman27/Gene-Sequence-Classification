import os

def extractName(file_path):

    # Extract the base filename
    filename = os.path.basename(file_path)

    # Split the filename by underscores and take the last word
    last_word = filename.split('_')[-1]

    # If the filename extension should be excluded
    last_word = last_word.split('.')[0]

    return last_word
