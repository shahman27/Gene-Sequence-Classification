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

for genome in file_paths:
    sequences = list(SeqIO.parse(genome, 'fasta'))
    # Example: Process and encode the first sequence
    if sequences:
        seq = sequences[0].seq
        encoded_seq = one_hot_encode(seq)
        encodings.append(encoded_seq)


print(encodings)