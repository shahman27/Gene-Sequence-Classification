import numpy as np

def splitData(data):
    # Shuffle the data randomly
    np.random.shuffle(data)

    # Calculate the split index
    split_idx = int(0.8 * len(data))  # 80% of the length of the array

    # Split the data into training and testing
    train_data = data[:split_idx]
    test_data = data[split_idx:]

    return train_data, test_data
