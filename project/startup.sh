#!/bin/bash
sudo apt-get update
sudo apt-get install python3-pip --assume-yes
sudo -H python3 -m pip install -U uwsgi
sudo -H python3 -m pip install -U pipenv
sudo apt-get install nginx --assume-yes
mkdir media
mkdir static
cd /home/ubuntu/app
pipenv install --system --deploy
sudo cp setup/nginx.conf /etc/nginx/sites-available/default
sudo cp setup/uwsgi_params /etc/nginx/sites-available/
python3 src/manage.py collectstatic --no-input --settings=project.settings.production
uwsgi --ini uwsgi.ini
sudo service nginx restart
touch /home/ubuntu/app/reload