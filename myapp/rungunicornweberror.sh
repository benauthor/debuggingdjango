#!/bin/sh
gunicorn myapp.wsgi_weberror:application
