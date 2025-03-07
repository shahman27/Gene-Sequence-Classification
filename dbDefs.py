from db import db

collection = db["dna_sequences"]

def pushToDb(dna_dict):
    for species, sequences in dna_dict.items():
        doc = {
            "species": species,
            "dna_sequences": sequences
        }
        result = collection.insert_one(doc)
        # print(f"Inserted {species} with _id: {result.inserted_id}")

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
