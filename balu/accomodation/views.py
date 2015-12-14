from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.context_processors import csrf
from .models import VirtualRoom

def accomodation(request):
    rooms = VirtualRoom.objects.all() 
    return render_to_response("accomodation.html",
                              locals(),
                              context_instance=RequestContext(request))


def room_details(request, slug):
    return render_to_response("room_details.html", {
        'room': get_object_or_404(VirtualRoom, slug=slug)
    },context_instance=RequestContext(request))


def checkavailable(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        from_date = request.POST.get('from_date', '')
        to_date = request.POST.get('to_date', '')
        adults = request.POST.get('adults', '')
        kids = request.POST.get('kids', '')

        return render_to_response("check-available.html",
                                  locals(),
                                  context_instance=RequestContext(request))
    else:
        return render_to_response("check-available.html",
                                  context_instance=RequestContext(request))

