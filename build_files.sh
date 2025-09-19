#!/bin/bash

# Pour Vercel uniquement
pip3 cache purge
pip3 install setuptools
pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
