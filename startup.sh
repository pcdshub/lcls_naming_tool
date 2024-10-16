#!/bin/bash


export ACCESS_LOG_FORMAT='%(h)s %(l)s %({REMOTE_USER}i)s %(t)s "%(r)s" "%(q)s" %(s)s %(b)s %(D)s'

export LCLS_NAMING_TOOL_TAXONS_DIR="/cds/group/pcds/pyps/apps/lcls_naming_tool/taxons"

export HOME_DIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

export PYTHONPATH="${HOME_DIR}/lcls_naming_tool"

source /cds/group/pcds/pyps/conda/venvs/lcls_naming_tool/bin/activate

cd "${HOME_DIR}/lcls_naming_tool/web"

exec gunicorn app:app -b 0.0.0.0:8319 \
       --log-level=${LOG_LEVEL} --capture-output --enable-stdio-inheritance \
       --timeout 300 --graceful-timeout 1 \
       --access-logfile - --access-logformat "${ACCESS_LOG_FORMAT}"
