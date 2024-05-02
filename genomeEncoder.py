from Bio import SeqIO
import numpy as np
from genomeFiles import get_file_names
from extractSpeciesName import extractName
from dotenv import load_dotenv
import os

load_dotenv()

def one_hot_encode(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    return np.array([mapping[s] for s in seq])

# Load sequences
file_directory = os.getenv('FILE_DIRECTORY')
file_paths = get_file_names(file_directory)

encodings = []

# for file in file_paths:
#     genome_dict = {}
#     with open(file, 'r') as file:
#         for sequence in SeqIO.parse(file, 'fasta'):        
#             # Example: Process and encode the first sequence
#             encoded_seq = one_hot_encode(sequence)
#             encodings.append(encoded_seq)

genome_dict = {}
species = extractName(file_paths[1])
current_file = file_paths[1]
with open(current_file, 'r') as file:
    for sequence in SeqIO.parse(file, 'fasta'):
        encoded_seq = one_hot_encode(sequence)
        encodings.append(encoded_seq)

new_data = {species: encodings[0]}
genome_dict.update(new_data)

print(genome_dict) 
    
# print(encodings)