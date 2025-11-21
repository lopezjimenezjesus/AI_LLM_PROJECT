#!/bin/bash

# This script handles the deployment of the model to Hugging Face.

# Load environment variables from the deployment configuration
source ../configs/deployment.yaml

# Check if the model directory exists
if [ ! -d "$MODEL_DIR" ]; then
  echo "Model directory does not exist. Please ensure the model is trained and saved."
  exit 1
fi

# Login to Hugging Face
echo "Logging in to Hugging Face..."
huggingface-cli login

# Upload the model to Hugging Face
echo "Uploading model to Hugging Face..."
transformers-cli upload --model_name "$MODEL_NAME" --model_dir "$MODEL_DIR"

# Check if the upload was successful
if [ $? -eq 0 ]; then
  echo "Model uploaded successfully to Hugging Face."
else
  echo "Failed to upload the model."
  exit 1
fi

# Optionally, update the model card
if [ -f "../huggingface/model_card.md" ]; then
  echo "Updating model card..."
  huggingface-cli update_model_card --model_name "$MODEL_NAME" --model_card "../huggingface/model_card.md"
fi

echo "Deployment to Hugging Face completed."