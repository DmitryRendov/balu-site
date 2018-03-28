# coding=utf-8
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext, ugettext_lazy as _
from models import ATTRIBUTE_CHOICES, Attribute, AttributeValue


# Create your views here.
class AttributeTypesForm(ModelForm):
    type = forms.CharField(max_length=15, widget=forms.Select(choices=ATTRIBUTE_CHOICES))
    name = forms.CharField(max_length=150)
    required = forms.BooleanField(required=False)
    value = forms.ModelChoiceField(queryset=AttributeValue.objects.all(), required=False)

    class Meta:
        model = Attribute
        fields = ['type', 'name', 'required']

@login_required
def attributes(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['attributes'] = Attribute.objects.all()

    return render_to_response("attributes.html",
                              args)
    pass

@login_required
def add_attribute(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = AttributeTypesForm()
    redirect_to = request.GET.get('back', reverse('inventory.views.show_inventory_classes'))
    if request.POST:
        form = AttributeTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_to)
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("add_attribute.html",
                              args)

@login_required
def edit_attribute(request, id):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = AttributeTypesForm(instance=Attribute.objects.get(id=id))
    args['back'] = request["back"]
    if request.POST:
        form = AttributeTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory.views.show_inventory_classes')
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("add_attribute.html",
                              args)

@login_required
def delete_attribute(request):
    pass
