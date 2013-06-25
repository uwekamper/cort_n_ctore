#!/bin/bash
set -e
LOGFILE=/home/uk/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=uk
GROUP=uk
cd /home/uk/cort_n_ctore/cort_n_ctore
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS \
	--pid /var/run/cort_n_ctore.pid \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE \
    --pythonpath=/home/uk/cort_n_ctore/cort_n_ctore \
    --settings="cort_n_ctore.settings_deploy"