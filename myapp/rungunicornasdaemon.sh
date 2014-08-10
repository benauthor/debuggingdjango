#!/bin/sh
gunicorn myapp.wsgi:application --timeout 3600 --daemon
