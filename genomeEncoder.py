from Bio import SeqIO
import numpy as np
from genomeFiles import get_file_names
from extractSpeciesName import extractName
from dotenv import load_dotenv
from splitData import splitData
from dbDefs import pushToDb
#from dbDefs import printDocs
from db import db
import os

load_dotenv()

def one_hot_encode(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    arr = np.array([mapping[s] for s in seq])
    return arr.tolist()


file_directory = os.getenv('FILE_DIRECTORY')
file_paths = get_file_names(file_directory)
collection = db["dna_sequences"]


genome_dict = {}
for file in file_paths:
    with open(file, 'r') as file_handle:
        species = extractName(file)
        doc = {
            "species": species,
            "dna_sequences": []
        }
        for sequence in SeqIO.parse(file_handle, 'fasta'):
            seq_str = str(sequence.seq)
            sub_doc = {"species": species, "dna_sequences": seq_str}
            collection.insert_one(sub_doc)
            
        # curr_data = {species: encodings}
        # genome_dict.update(curr_data)

# def pushToDb(dna_dict):
#     for species, sequences in dna_dict.items():
#         doc = {
#             "species": species,
#             "dna_sequences": sequences
#         }
#         result = collection.insert_one(doc)
#         # print(f"Inserted {species} with _id: {result.inserted_id}")

# for key, val in genome_dict.items():
#     print(key)
#     arr = val[:1]
#     arr2 = []
#     for a in arr:
#         arr2.append(a[:5])
#     print(arr2)

#pushToDb(genome_dict)

def printDocs():
    # print("printing docs:")
    # for doc in collection.find():
    #     print(doc)
    # Suppose 'collection' refers to your MongoDB collection
    doc_count = collection.count_documents({})
    print(f"Total documents in the collection: {doc_count}")

    if doc_count == 4:
        print("All 4 documents are present!")
    else:
        print("Some documents might be missing.")

printDocs()

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