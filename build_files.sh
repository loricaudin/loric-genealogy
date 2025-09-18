#!/bin/bash

# Pour Vercel uniquement
mkdir -p staticfiles
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput

ls /vercel/path0
ls /vercel/output