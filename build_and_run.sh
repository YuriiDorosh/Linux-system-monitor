#!/bin/bash

# Step 1: Installing dependencies
sudo apt update
sudo apt install -y ffmpeg git python3 python3-pip

# Checking if the repository is already cloned
if [ -d "Linux-system-monitor" ]; then
  echo "The repository has already been cloned, let's proceed to the next steps."
else
  # Step 2: Clone the repository
  git clone https://github.com/YuriiDorosh/Linux-system-monitor.git
fi

# Step 3: Go to the directory with the application
cd Linux-system-monitor/

# Step 4: Create and activate the virtual environment
python3 -m venv env
source env/bin/activate

# Step 5: Installing the required Python packages
pip3 install -r requirements.txt

# Step 6: Launch the project
cd src/
python3 main.py