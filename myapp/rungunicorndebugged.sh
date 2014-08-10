#!/bin/sh
gunicorn myapp.wsgi_debugged:application
