from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import yaml

def load_model_and_tokenizer(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_response(model, tokenizer, prompt: str, max_length: int = 50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=max_length)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    # Load configuration
    with open("configs/inference.yaml", 'r') as config_file:
        config = yaml.safe_load(config_file)

    model_name = config['model_name']
    prompt = config['prompt']
    max_length = config.get('max_length', 50)

    # Load model and tokenizer
    model, tokenizer = load_model_and_tokenizer(model_name)

    # Generate response
    response = generate_response(model, tokenizer, prompt, max_length)
    print("Generated Response:", response)

if __name__ == "__main__":
    main()