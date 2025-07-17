#!/bin/bash

echo "🛡️ CyberScrape Toolkit: Advanced Web Scraping for Security Professionals"
echo "======================================================================="
echo "Select a target module:"
echo "1. Basic HTML Scraper"
echo "2. Email Harvester"
echo "3. Scrape with Proxy"
echo "4. JavaScript DOM Scraper (Selenium)"
echo "5. Deep Metadata & File Extractor"
echo "======================================================================="
read -p "Enter your choice (1-5): " choice

read -p "Enter the target URL: " url

# Setup Python virtual environment
if [ ! -d "venv" ]; then
  echo "🔧 Creating virtual environment..."
  python3 -m venv venv || { echo "❌ Python3 not found"; exit 1; }
fi

source venv/bin/activate

# Install dependencies
echo "📦 Installing required Python packages..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt > /dev/null

# Ensure ChromeDriver is installed for Selenium (module 4)
if [ "$choice" -eq 4 ]; then
  if ! command -v chromedriver &> /dev/null; then
    echo "🌐 ChromeDriver not found. Installing dependencies..."

    sudo apt update
    sudo apt install -y chromium-browser chromium-chromedriver > /dev/null 2>&1

    if [ -f "/usr/lib/chromium-browser/chromedriver" ]; then
      sudo ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
    elif [ -f "/usr/lib/chromium/chromedriver" ]; then
      sudo ln -sf /usr/lib/chromium/chromedriver /usr/bin/chromedriver
    else
      echo "❌ ChromeDriver still not found. Please install manually or specify the path in selenium_js.py."
      exit 1
    fi
  fi
fi

# Run the appropriate module
case $choice in
  1)
    python3 scraper_modules/basic.py "$url"
    ;;
  2)
    python3 scraper_modules/email.py "$url"
    ;;
  3)
    read -p "Enter proxy (IP:PORT): " proxy
    python3 scraper_modules/proxy.py "$url" "$proxy"
    ;;
  4)
    python3 scraper_modules/selenium_js.py "$url"
    ;;
  5)
    python3 scraper_modules/deep_metadata.py "$url"
    ;;
  *)
    echo "❌ Invalid selection."
    ;;
esac
