import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(raw_data_path, processed_data_path, splits_dir, test_size=0.2, val_size=0.1):
    # Load raw data
    with open(raw_data_path, 'r') as f:
        raw_data = f.readlines()

    # Process raw data (example: stripping whitespace and converting to JSON)
    processed_data = [{'text': line.strip()} for line in raw_data if line.strip()]

    # Save processed data to JSON Lines format
    with open(processed_data_path, 'w') as f:
        for entry in processed_data:
            f.write(json.dumps(entry) + '\n')

    # Split the data into train, validation, and test sets
    train_data, test_data = train_test_split(processed_data, test_size=test_size)
    val_data, test_data = train_test_split(test_data, test_size=val_size/(test_size + val_size))

    # Save splits
    with open(os.path.join(splits_dir, 'train.jsonl'), 'w') as f:
        for entry in train_data:
            f.write(json.dumps(entry) + '\n')

    with open(os.path.join(splits_dir, 'val.jsonl'), 'w') as f:
        for entry in val_data:
            f.write(json.dumps(entry) + '\n')

    with open(os.path.join(splits_dir, 'test.jsonl'), 'w') as f:
        for entry in test_data:
            f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    raw_data_path = '../data/raw/dataset.txt'  # Adjust path as necessary
    processed_data_path = '../data/processed/dataset.jsonl'
    splits_dir = '../data/splits'

    prepare_data(raw_data_path, processed_data_path, splits_dir)