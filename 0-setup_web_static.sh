#!/bin/bash

# Update package lists (good practice before installations)
sudo apt update

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
  sudo apt install -y nginx
fi

# Create all necessary directories with a single command
sudo mkdir -p /data/web_static/{releases,shared,releases/test}

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Remove any existing symbolic link before creating a new one
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Create a separate configuration file for clarity and maintainability
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/hbnb_static
sudo sed -i 's/server_name _;/server_name localhost; alias hbnb_static;/' /etc/nginx/sites-available/hbnb_static

# Enable the new configuration and restart Nginx
sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo systemctl restart nginx

exit 0

