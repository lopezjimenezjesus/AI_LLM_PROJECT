def load_model(model_name):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    return model, tokenizer

def preprocess_data(data):
    # Implement data preprocessing steps here
    processed_data = []
    for item in data:
        # Example preprocessing step
        processed_data.append(item.strip())
    return processed_data

def save_model(model, tokenizer, save_directory):
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)

def load_data(file_path):
    import json

    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    return data

def split_data(data, train_ratio=0.8, val_ratio=0.1):
    import numpy as np

    np.random.shuffle(data)
    train_size = int(len(data) * train_ratio)
    val_size = int(len(data) * val_ratio)

    train_data = data[:train_size]
    val_data = data[train_size:train_size + val_size]
    test_data = data[train_size + val_size:]

    return train_data, val_data, test_data

def set_seed(seed):
    import random
    import numpy as np
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)