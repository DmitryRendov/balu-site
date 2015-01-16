from inventory.models import Inventory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def show_inventory_classes(request):
    return render_to_response("inventory.html",
                              {'nodes': Inventory.objects.all(), 'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))

def home_page(request):
    return render_to_response("base.html",
                              {'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))


@login_required
def edit_inventory(request, id):
    return render_to_response("edit.html",
                              {'id' : id, 'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))