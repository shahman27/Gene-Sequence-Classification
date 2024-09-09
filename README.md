# Gene Sequence Classifier

This project focuses on the classification of DNA sequences from humans, bacteria, viruses, and fungi using a Transformer model built with PyTorch and BioPython. The project aims at species identification, achieving a 75% accuracy rate. The pipeline includes custom encoding of genetic data, efficient data storage, and retrieval using SQL databases for scalability and integrity.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Gene Sequence Classifier** differentiates between DNA sequences from various species. It leverages a Transformer model to accurately classify sequences as human, bacterial, viral, or fungal, achieving a 75% accuracy rate. The project also includes the development of a custom encoding for genetic data, enabling efficient storage and retrieval through an SQL database. This solution enhances scalability and data integrity by 3x.

## Features

- Transformer-based model for DNA sequence classification.
- Encodes genetic sequences for efficient storage and retrieval.
- Supports species identification across human, bacterial, viral, and fungal DNA sequences.
- SQL database integration for scalable and robust data handling.

## Tech Stack

- **Languages**: Python
- **Libraries**: PyTorch, BioPython, NumPy
- **Database**: SQL
- **Data Handling**: Custom genetic data encoding

## Setup

To set up this project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/gene-sequence-classifier.git
   cd gene-sequence-classifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the SQL database:
   - Follow the instructions in `genomeFiles.py` to initialize and structure the database for storing and retrieving encoded DNA sequences.

4. Run the model:
   - Prepare your dataset and split it using `splitData.py`.
   - Train the model using `extractSpeciesName.py` and adjust parameters as needed.

## How to Use

1. **Prepare DNA Sequences**:
   Place your DNA sequence data into the appropriate folder and ensure it is formatted correctly.

2. **Encode Data**:
   Use `genomeEncoder.py` to encode the sequences into a format suitable for the model.

3. **Run Model**:
   Execute the training script in `extractSpeciesName.py` to start training the Transformer model. You can monitor the training process and adjust hyperparameters for better accuracy.

4. **Evaluate Results**:
   After training, the model outputs species classification results, which can be further analyzed for precision and recall.

## Model Details

The Transformer model processes DNA sequences and outputs a classification of the species (human, bacterial, viral, or fungal). The model architecture is designed to handle large genetic datasets efficiently, and its accuracy improves with better-preprocessed data and increased training time.

- **Input**: DNA sequences in encoded format.
- **Output**: Species classification.
- **Accuracy**: 75% on the current dataset.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or raise issues for any bugs or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
