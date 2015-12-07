from django.shortcuts import render_to_response
from django.template import RequestContext
from accomodation.models import VirtualRoom
from album.models import Image

# Create your views here.
def index(request):
    try:
        favrooms = VirtualRoom.objects.filter(featured=True)
    except VirtualRoom.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('landing.html', locals(), context_instance=RequestContext(request))
