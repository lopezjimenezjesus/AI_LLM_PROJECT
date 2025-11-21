import pytest
import json

from src.utils import load_data, preprocess_data

def test_load_data():
    # Test loading the dataset
    data = load_data('data/processed/dataset.jsonl')
    assert isinstance(data, list)
    assert len(data) > 0

def test_preprocess_data():
    # Test preprocessing of data
    raw_data = [
        {"text": "This is a test.", "label": 1},
        {"text": "Another test.", "label": 0}
    ]
    processed_data = preprocess_data(raw_data)
    assert isinstance(processed_data, list)
    assert all('input_ids' in item for item in processed_data)
    assert all('attention_mask' in item for item in processed_data)