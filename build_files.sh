#!/bin/bash

# Pour Vercel uniquement
mkdir -p staticfiles
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput

echo Contenu vercel :
ls /vercel/
echo Contenu / :
ls /