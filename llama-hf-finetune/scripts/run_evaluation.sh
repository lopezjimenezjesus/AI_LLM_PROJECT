#!/bin/bash

# Activate the virtual environment
source ../venv/bin/activate

# Set the model and data paths
MODEL_PATH="path/to/your/fine-tuned/model"
DATA_PATH="../data/splits/val.jsonl"

# Run the evaluation script
python ../src/evaluate.py --model_path $MODEL_PATH --data_path $DATA_PATH --output_path ../experiments/evaluation_results.json

# Deactivate the virtual environment
deactivate