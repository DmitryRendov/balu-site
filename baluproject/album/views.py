from album.models import Album
from django.shortcuts import render_to_response
from django.template import RequestContext

def show_album(request):
    return render_to_response("album.html",
                              {'nodes': Album.objects.all()},
                              context_instance=RequestContext(request))