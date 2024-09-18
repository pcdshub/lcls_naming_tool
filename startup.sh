#!/bin/bash


export ACCESS_LOG_FORMAT='%(h)s %(l)s %({REMOTE_USER}i)s %(t)s "%(r)s" "%(q)s" %(s)s %(b)s %(D)s'

source pcds_conda

pip3 install -r requirements.txt

python3 -m venv venv

source venv/bin/activate

cd lcls_naming_tool/web

rm lcls_naming_tool.py

rm -rf taxons

cp ../lcls_naming_tool.py .

cp -r ../taxons .

export FLASK_APP=app

flask --app app run

gunicorn --config gunicorn_config.py app:app

--log-level=${LOG_LEVEL} --capture-output --enable-stdio-inheritance \
--timeout 300 --graceful-timeout 1 \
--access-logfile - --access-logformat "${ACCESS_LOG_FORMAT}"