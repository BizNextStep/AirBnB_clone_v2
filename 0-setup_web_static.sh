nstall Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create directory structure if it doesn't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sudo sed -i "/^}/i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "$config_file"

# Restart Nginx
sudo service nginx restart

exit 0

