#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
 <head>
   <title>
   Holberton School (title)
   </title>
 </head>
 <body>
   Holberton School (body)
 </body>
 </html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a \tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\tautoindex off;\n}' /etc/nginx/sites-available/default
service nginx restart
exit 0
