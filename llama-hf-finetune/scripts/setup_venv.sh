#!/bin/bash

# This script sets up a Python virtual environment for the LLaMa fine-tuning project.

# Define the name of the virtual environment
VENV_NAME=".venv"

# Create a virtual environment
python -m venv $VENV_NAME

# Activate the virtual environment
source $VENV_NAME/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the required packages
pip install -r requirements.txt

echo "Virtual environment setup complete. Activate it using 'source $VENV_NAME/bin/activate'."