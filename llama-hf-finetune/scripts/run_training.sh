#!/bin/bash

# Activate the virtual environment
source ../venv/bin/activate

# Set the configuration file for training
CONFIG_FILE="../configs/training.yaml"

# Run the training script
python ../src/train.py --config $CONFIG_FILE

# Deactivate the virtual environment
deactivate