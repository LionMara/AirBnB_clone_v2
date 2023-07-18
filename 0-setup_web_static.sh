#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static/

# install nginx if not installed already
if ! command -v nginx >/dev/null 2>&1;then
    apt-get update
    apt-get install -y nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# create an html
echo "<!DOCTYPE html>
<html>
<head>
</head>
<body>
<p>Nginx server test</p>
</body>
</html>" | tee /data/web_static/releases/index.html

# create sym link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data to ubuntu and group
chown -R ubuntu:ubuntu /data/

# update nginx config
config_file="/etc/nginx/sites-enabled/default"

# add alias to serve content
sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' "$config_file"

# restart nginx
service nginx restart
