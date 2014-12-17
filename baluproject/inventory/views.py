from django.shortcuts import render
from inventory.models import Inventory
from django.shortcuts import render_to_response
from django.template import RequestContext

def show_inventory_classes(request):
    return render_to_response("inventory.html",
                               {'nodes':Inventory.objects.all()},
                               context_instance=RequestContext(request))