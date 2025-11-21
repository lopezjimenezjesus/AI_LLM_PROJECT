import os
import json
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer
from torch.utils.data import DataLoader
from datasets import load_dataset

def load_data(data_dir):
    train_data = load_dataset('json', data_files=os.path.join(data_dir, 'splits', 'train.jsonl'))
    val_data = load_dataset('json', data_files=os.path.join(data_dir, 'splits', 'val.jsonl'))
    return train_data, val_data

def create_dataloader(dataset, batch_size):
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)

def train_model(model, dataloader, optimizer, device, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for batch in dataloader:
            inputs = batch['input_ids'].to(device)
            labels = batch['labels'].to(device)

            optimizer.zero_grad()
            outputs = model(inputs, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}')

def save_model(model, output_dir):
    model.save_pretrained(output_dir)

def main():
    data_dir = './data'
    output_dir = './models/llama_finetuned'
    num_epochs = 3
    batch_size = 8
    learning_rate = 5e-5

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    tokenizer = LlamaTokenizer.from_pretrained('huggingface/llama')
    model = LlamaForCausalLM.from_pretrained('huggingface/llama').to(device)

    train_data, val_data = load_data(data_dir)
    train_loader = create_dataloader(train_data['train'], batch_size)

    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    train_model(model, train_loader, optimizer, device, num_epochs)
    save_model(model, output_dir)

if __name__ == '__main__':
    main()