#!/bin/bash

# Pour Vercel uniquement
pip3 install -r requirements.txt
mkdir -p public/static
python3 manage.py collectstatic --noinput