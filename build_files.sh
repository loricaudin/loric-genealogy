#!/bin/bash

# Pour Vercel uniquement
pip install -r requirements.txt
mkdir -p public/static
python manage.py collectstatic --noinput