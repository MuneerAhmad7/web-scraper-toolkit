#!/bin/bash

echo "🔧 Setting up Web Scraper CyberSec Environment..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Ensure Chromedriver for Selenium (optional)
if ! command -v chromedriver &> /dev/null; then
    echo "💻 Installing ChromeDriver for Selenium..."
    sudo apt install -y chromium-chromedriver
    sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin
fi

echo "✅ Setup complete. Activate env with: source venv/bin/activate"
