#!/bin/sh
gunicorn myapp.wsgi_werkzeug:application
