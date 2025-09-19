#!/bin/bash

# Pour Vercel uniquement
echo DEBUT BUILD VERCEL

pip3 cache purge
pip3 install setuptools
pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

echo FIN BUILD VERCEL