from Bio import SeqIO
import numpy as np

def one_hot_encode(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    return np.array([mapping[s] for s in seq])

# Load sequences
file_path = 'yourfile.fna'
sequences = list(SeqIO.parse(file_path, 'fasta'))

# Example: Process and encode the first sequence
if sequences:
    seq = sequences[0].seq
    encoded_seq = one_hot_encode(seq)
    print(encoded_seq)
