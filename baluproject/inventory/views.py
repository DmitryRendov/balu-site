from inventory.models import Inventory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms


def show_inventory_classes(request):
    return render_to_response("inventory.html",
                              {'nodes': Inventory.objects.all()},
                              context_instance=RequestContext(request))

def home_page(request):
    return render_to_response("base.html",
                              context_instance=RequestContext(request))


def auth_page(request):
    return render_to_response("login.html",
                              context_instance=RequestContext(request))


class InventoryForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    #is_container = forms.BooleanField(default=False)

def edit_inventory(request, id):
    return render_to_response("edit.html",
                              {'id' : id},
                              context_instance=RequestContext(request))