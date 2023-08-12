#!/bin/bash

# Define function to determine the package manager
determinePackageManager() {
    if command -v apt > /dev/null; then
        PKG_MANAGER="apt"
        UPDATE_CMD="sudo apt update"
        INSTALL_CMD="sudo apt install -y"
    elif command -v pacman > /dev/null; then
        PKG_MANAGER="pacman"
        UPDATE_CMD="sudo pacman -Syu"
        INSTALL_CMD="sudo pacman -S --noconfirm"
    elif command -v yum > /dev/null; then
        PKG_MANAGER="yum"
        UPDATE_CMD="sudo yum update -y"
        INSTALL_CMD="sudo yum install -y"
    else
        echo "Unsupported package manager. Exiting."
        exit 1
    fi
}

# Update and install packages
installPackages() {
    $UPDATE_CMD || true
    $INSTALL_CMD ffmpeg scrot git python3 python3-tk pip3 || true
}

# Clone repository and setup virtual environment
setupProject() {
    python3 -m venv env || true
    source env/bin/activate || true
    pip3 install -r requirements.txt || true
}

# Prompt user to run the project
promptForProjectExecution() {
    read -p "Would you like to run the project now? [y/n]: " run_now
    if [[ "$run_now" == "y" ]]; then
        cd src/ || true
        echo "How would you like to run the project?"
        echo "1. Greeting window"
        echo "2. GUI Version"
        echo "3. Console version"
        echo "4. Settings"
        read -p "Choose a number [1-4]: " choice
        case $choice in
            1) python3 main.py ;;
            2) python3 main.py -g ;;
            3) python3 main.py -c ;;
            4) python3 main.py --settings ;;
            *) echo "Invalid choice. Exiting." ;;
        esac
    fi
}

# Main execution
determinePackageManager
installPackages
setupProject
promptForProjectExecution

echo "Script has finished its work. Please ensure all dependencies, packages, etc. are correctly installed."
