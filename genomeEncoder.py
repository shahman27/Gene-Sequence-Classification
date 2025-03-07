from Bio import SeqIO
import numpy as np
from genomeFiles import get_file_names
from extractSpeciesName import extractName
from dotenv import load_dotenv
from splitData import splitData
import os

load_dotenv()

def one_hot_encode(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    return np.array([mapping[s] for s in seq])

# Load sequences
file_directory = os.getenv('FILE_DIRECTORY')
file_paths = get_file_names(file_directory)


genome_dict = {}
for file in file_paths:
    with open(file, 'r') as file_handle:
        encodings = []
        species = extractName(file)
        for sequence in SeqIO.parse(file_handle, 'fasta'):        
            # Example: Process and encode the first sequence
            encoded_seq = one_hot_encode(sequence)
            encodings.append(encoded_seq)
        curr_data = {species: encodings}
        genome_dict.update(curr_data)
    
# print(genome_dict.keys())
# genome_dict = {}
# species = extractName(file_paths[1])
# current_file = file_paths[1]
# with open(current_file, 'r') as file:
#     for sequence in SeqIO.parse(file, 'fasta'):
#         encoded_seq = one_hot_encode(sequence)
#         encodings.append(encoded_seq)

# new_data = {species: encodings[0]}
# genome_dict.update(new_data)

# test_data, train_data = splitData(encodings)

# test_train_data = {'test': test_data, 'train': train_data}

# print(genome_dict) 
    
# print(encodings)