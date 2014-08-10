from django.http import HttpResponse

def index(request):
    return HttpResponse("This works.")

def pdb_view(request):
    """
    Here we just use good ol' pdb. This works fine if you ran the
    server from your console and can go back there to poke at it
    interactively. But if you've run the server as a daemon, you got
    no place to look.
    """
    import pdb; pdb.set_trace()
    return HttpResponse("This works.")

def rpdb_view(request):
    """
    rpdb solves that problem: it starts a server so you can just telnet into
    the interactive session you expected.
    """
    import rpdb; rpdb.set_trace()
    return HttpResponse("This works.")

def oops(request):
    """
    Here we just break the code and see whatever the setup gives us in the
    browser. Hoping for the werkzeug debugger niceness.
    """
    asdf
    return HttpResponse("This works.")
