#!/bin/bash


export ACCESS_LOG_FORMAT='%(h)s %(l)s %({REMOTE_USER}i)s %(t)s "%(r)s" "%(q)s" %(s)s %(b)s %(D)s'

source /cds/group/pcds/pyps/conda/venvs/lcls_naming_tool/bin/activate

python -m pip install --upgrade pip

pip install gunicorn

exec gunicorn start:app -b 0.0.0.0:8319 \
       --log-level=${LOG_LEVEL} --capture-output --enable-stdio-inheritance \
       --timeout 300 --graceful-timeout 1 \
       --access-logfile - --access-logformat "${ACCESS_LOG_FORMAT}"