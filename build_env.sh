#!/bin/bash

# Install system packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install virtualenv
sudo -H pip3 install virtualenv

# Create virtual environment
virtualenv venv
source venv/bin/activate

# Install python packages
pip install -r requirements.txt