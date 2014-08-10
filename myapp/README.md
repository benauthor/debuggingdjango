# Debugging Django

Coming into a situation where I need to debug a Django application
running gunicorn daemonized, I sorely missed the tools i'm used to,
which were:

1. pdb. since i'm not running a dev server from a terminal, I can't
just drop a pdb breakpoint and go start debugging.

2. in-browser debugging. Paste and Werkzeug both have nifty debug-mode
error screens. So handy!

This repo shows three routes to debugging bliss.

## PDB

The obvious one, which you already know. The motivation for this
project was that this obvious solution was unavailable in my
setup. But if you do have access to an interactive console where you
start the development server, this option is available to you. Simply
add the line `import pdb; pdb.set_trace()` in your code where you'd
like to start debugging, and visit the URL that triggers that code
path. You'll probably want to up your request timeout to give you some
breathing room.

In this demo, start by running

    cd myapp
    ./runwithgunicorn.sh

then visit `http://localhost:8000/demo/pdb/` in your browser and look
back in your terminal: pdb is ready to use.

## RPDB

So if you can't  get back to an interactive console, how  do you see a
debugger? Rpdb is  a simple yet brilliant project that  wraps PDB in a
simple  server and  serves  the  debugging shell  on  a  port on  your
localhost.  Again, be  sure to  up your  sever's timeout  to something
large so you have time to debug. To demo:

    cd myapp
    ./rungunicornasdaemon.sh

visit `http://localhost:8000/demo/rpdb/` and then

    nc localhost 4444

Now you are in a pdb session! Nice!

## Werkzeug

You can use Werkzeug's DebuggedApplication middleware to replace Django's
lame default debug-mode error page. Check out myapp/wsgi_debugged.py to see
how that works. To demo:

    ./rungunicorndebugged.sh

and visit `http://localhost:8000/demo/oops/`, whose view has an intentional
error that triggers the nice in-browser debugger.