#!/bin/bash

# Linux System Monitor Build and Run Script

# Step 1: Install dependencies
sudo apt update
sudo apt install -y ffmpeg git python3 python3-pip

# Step 2: Check if the repository is already cloned
if [ -d "Linux-system-monitor" ]; then
  echo "The repository has already been cloned, let's proceed to the next steps."
else
  # Clone the repository
  git clone https://github.com/YuriiDorosh/Linux-system-monitor.git
  # Go to the directory with the application
  cd Linux-system-monitor/
fi

# Step 3: Create and activate the virtual environment
python3 -m venv env
source env/bin/activate

# Step 4: Install the required Python packages
pip3 install -r requirements.txt

# Step 5: Launch the project
cd src/

# Display menu with options
echo "Select the version to run:"
echo "1) GUI version"
echo "2) Console version"
echo "3) Default version (Greeting window)"
echo "4) Help - Display project help"

# Read user input for the desired version
read -p "Enter your choice [1-4]: " choice

# Execute the selected option
case $choice in
  1)
    python3 main.py --gui
    ;;
  2)
    python3 main.py --console
    ;;
  3)
    python3 main.py
    ;;
  4)
    python3 main.py --help
    ;;
  *)
    echo "Invalid choice. Exiting."
    ;;
esac
