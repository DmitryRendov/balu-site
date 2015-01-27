# coding=utf-8
from django.core.context_processors import csrf
from models import Inventory
from attribute import AttributeType
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext, ugettext_lazy as _
from mptt.forms import TreeNodeChoiceField
from mptt.models import MPTTModel
from attribute import ATTRIBUTE_CHOICES, AttributeValue

@login_required(login_url='/auth/login/')
def show_inventory_classes(request):
    return render_to_response("inventory.html",
                              {'nodes': Inventory.objects.all(), 'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))

class InventoryForm(ModelForm):
    name = forms.CharField(label="Класс", max_length=200, help_text="Укажите имя класса")
    description = forms.CharField(label="Описание", required=False)
    parent = TreeNodeChoiceField(queryset=Inventory.objects.all(), required=False)
    attributes = forms.ModelMultipleChoiceField(queryset=AttributeType.objects.all(), required=False)

    class Meta:
        model = Inventory
        fields = ['name', 'parent', 'description', 'attributes']

@login_required
def edit_inventory(request, id):

    instance=Inventory.objects.get(id=id)
    args = {}
    args.update(csrf(request))
    args['id'] = id
    args['username'] = auth.get_user(request).username
    args['form'] = InventoryForm(instance=instance)
    if request.POST:
        form = InventoryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('inventory.views.show_inventory_classes')
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("edit.html",
                              args)

@login_required
def add_inventory(request):

    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = InventoryForm()
    if request.POST:
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory.views.show_inventory_classes')
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("edit.html",
                              args)


@login_required
def delete_inventory(request, id):

    args={}
    args['username'] = auth.get_user(request).username
    instance = Inventory.objects.get(id=id)
    if instance is not None:
        if MPTTModel.delete(instance):
            args['status'] = 'Узел и его потомки успешно удалён'
        else:
            args['status'] = 'Произошла ошибка при удалении узла. Попробуйте еще раз.'
    else:
        args['status'] = 'Невозможно удалить выбранный узел!'

    return redirect('inventory.views.show_inventory_classes')

class AttributeTypesForm(ModelForm):
    type = forms.CharField(max_length=15, widget=forms.Select(choices=ATTRIBUTE_CHOICES))
    name = forms.CharField(max_length=150)
    required = forms.BooleanField(required=False)
    value = forms.ModelChoiceField(queryset=AttributeValue.objects.all(), required=False)

    class Meta:
        model = Inventory
        fields = ['type', 'name', 'required', 'value']

@login_required
def attributes(request, id):
    args = {}
    args.update(csrf(request))
    args['id'] = id
    args['username'] = auth.get_user(request).username
    args['form'] = AttributeTypesForm()
    if request.POST:
        form = AttributeTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory.views.edit_inventory', id=id)
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("add_attribute.html",
                              args)

def home_page(request):
    return render_to_response("base.html",
                              {'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))


