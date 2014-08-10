# The default stuff
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# then you have to override Django's own debug response
# to let the error keep bubbling
import django.views.debug

def null_technical_500_response(request, exc_type, exc_value, tb):
    raise exc_type, exc_value, tb
django.views.debug.technical_500_response = null_technical_500_response

# and wrap the application in paste's weberror

from weberror.evalexception import make_eval_exception
global_conf = {} # see weberror docs for options...
application = make_eval_exception(application, global_conf)
