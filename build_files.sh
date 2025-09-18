#!/bin/bash

# Pour Vercel uniquement
mkdir -p staticfiles
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput

echo Contenu path0 :
ls /vercel/path0
echo Contenu output :
ls /vercel/output