#!/bin/bash
set -e
LOGFILE=/home/suitmedia/ivan/mysite/log/s_err.log
LOGDIR=$(dirname $LOGFILE)
cd /home/suitmedia/ivan/mysite
source /usr/local/bin/virtualenvwrapper.sh
workon poll
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -c gunicorn.py --log-file=$LOGFILE