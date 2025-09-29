#!/bin/bash
# filepath: setup_env.sh

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Virtual environment activated and dependencies installed."

deactivate

echo "Virtual environment deactivated."