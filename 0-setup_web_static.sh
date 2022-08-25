#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "
<html>
 <head>
   <title>
   Holberton School (title)
   </title>
 </head>
 <body>
   Holberton School (body)
 </body>
 </html>" > sudo /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
