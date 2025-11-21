#!/bin/bash

# This script uploads the fine-tuned model to Hugging Face Model Hub.

MODEL_NAME="your_model_name"  # Replace with your model name
MODEL_PATH="./path_to_your_model"  # Replace with the path to your fine-tuned model
HUGGINGFACE_TOKEN="your_huggingface_token"  # Replace with your Hugging Face token

# Login to Hugging Face
echo "Logging in to Hugging Face..."
huggingface-cli login --token $HUGGINGFACE_TOKEN

# Upload the model
echo "Uploading model to Hugging Face..."
transformers-cli upload $MODEL_PATH --model_id $MODEL_NAME

echo "Model uploaded successfully!"