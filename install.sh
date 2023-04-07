#!/bin/bash

# Install system dependencies
apt-get update && apt-get install -y git

# Clone the project
git clone https://github.com/Craxti/Network-Analysis.git
cd Network-Analysis

# Install project dependencies
pip install -r requirements.txt

# Run the project
python main.py
