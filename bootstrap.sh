#!/bin/bash

# install ollama if not installed
if ollama -h > /dev/null 2>&1; then
    echo "Ollama is already installed."
else
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# install python3.11 if not installed
if python3.11 --version > /dev/null 2>&1; then
    echo "Python 3.11 is already installed."
else
    echo "Installing Python 3.11..."
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3.11-dev
fi
# install venv if not installed 
if python3.11 -m venv --help > /dev/null 2>&1; then
    echo "Venv is already installed."
else
    echo "Installing Venv..."
    sudo apt install -y python3.11-venv
fi

# Create virtual environment if not exists
if [ -f "./venv/bin/activate" ]; then
    echo "Virtual environment exists."
else
    echo "Creating virtual environment..."
    python3.11 -m venv venv
fi
# Activate virtual environment
source venv/bin/activate

# Install llm-benchmark
pip install llm-benchmark
