from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.context_processors import csrf

def accomodation(request):
    return render_to_response("accomodation.html",
                              context_instance=RequestContext(request))

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

