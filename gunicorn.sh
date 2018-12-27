#!/bin/bash
cd /opt/tramites
source venv/bin/activate
cd /opt/tramites/tramites
gunicorn tramites.wsgi -t 600 -b 127.0.0.1:8004 -w 6 --user=servidor --group=servidor --log-file=/opt/tramites/gunicorn.log 2>>/opt/tramites/gunicorn.log

