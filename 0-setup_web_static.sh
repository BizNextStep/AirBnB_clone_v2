#!/usr/bin/env bash

# Set configurable variables
nginx_config="/etc/nginx/sites-available/default"
web_static_dir="/data/web_static"
html_content="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"

# Function for logging
log() {
    echo "$(date) - $1"
}

# Error handling function
handle_error() {
    log "Error: $1"
    exit 1
}

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    log "Nginx not found. Installing Nginx..."
    sudo apt-get update || handle_error "Failed to update packages"
    sudo apt-get install -y nginx || handle_error "Failed to install Nginx"
fi

# Create directory structure if it doesn't exist
mkdir -p "$web_static_dir/releases/test" "$web_static_dir/shared" || handle_error "Failed to create directories"

# Create a fake HTML file
echo -e "$html_content" | sudo tee "$web_static_dir/releases/test/index.html" || handle_error "Failed to create HTML file"

# Create symbolic link
ln -sf "$web_static_dir/releases/test/" "$web_static_dir/current" || handle_error "Failed to create symbolic link"

# Set ownership
sudo chown -R ubuntu:ubuntu "$web_static_dir" || handle_error "Failed to set ownership"

# Update Nginx configuration
sudo sed -i "/^}/i \\\tlocation /hbnb_static/ {\n\t\talias $web_static_dir/current/;\n\t}" "$nginx_config" || handle_error "Failed to update Nginx configuration"

# Restart Nginx
sudo service nginx restart || handle_error "Failed to restart Nginx"

log "Web server setup completed successfully"
exit 0

