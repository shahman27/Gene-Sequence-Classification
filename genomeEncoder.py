from Bio import SeqIO
import numpy as np
from genomeFiles import get_file_names

def one_hot_encode(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    return np.array([mapping[s] for s in seq])

# Load sequences
file_directory = '/Users/dhruvshah/Projects/Gene-Sequencing-Model/Gene-Sequence-Classification/Genome Sequences/'
file_paths = get_file_names(file_directory)

encodings = []

# for file in file_paths:
#     genome_dict = {}
#     with open(file, 'r') as file:
#         for sequence in SeqIO.parse(file, 'fasta'):        
#             # Example: Process and encode the first sequence
#             encoded_seq = one_hot_encode(sequence)
#             encodings.append(encoded_seq)

current_file = file_paths[1]
with open(current_file, 'r') as file:
    for sequence in SeqIO.parse(file, 'fasta'):
        encoded_seq = one_hot_encode(sequence)
        encodings.append(encoded_seq)


print(file_paths[1])
print(encodings[0]) 
    
# print(encodings)