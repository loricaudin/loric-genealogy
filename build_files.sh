#!/bin/bash

# Pour Vercel uniquement
mkdir -p staticfiles
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput

mkdir -p /vercel/output/static
cp -r staticfiles/* /vercel/output/static/