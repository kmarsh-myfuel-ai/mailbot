#!/bin/bash
read -p "deactivate first!"
rm -rf venv
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name migrations -exec rm -rf {} +
python3 -m venv venv
source venv/bin/activate
pip install -r mailbot/requirements.txt