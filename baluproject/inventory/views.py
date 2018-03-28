# coding=utf-8
from django.core.context_processors import csrf
from inventory.models import Inventory
from attributes.models import Attribute
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext, ugettext_lazy as _
from mptt.forms import TreeNodeChoiceField
from mptt.models import MPTTModel

@login_required(login_url='/auth/login/')
def show_inventory_classes(request, status = None):
    args = {}
    if status:
        args['status'] = status
    args['nodes'] = Inventory.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response("inventory.html",
                              args,
                              context_instance=RequestContext(request))

class InventoryForm(ModelForm):
    name = forms.CharField(label="Класс", max_length=200, help_text="Укажите имя класса")
    description = forms.CharField(label="Описание", required=False)
    parent = TreeNodeChoiceField(queryset=Inventory.objects.all(), required=False)
    attrs = forms.ModelMultipleChoiceField(queryset=Attribute.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label="Доступные атрибуты:")
    class Meta:
        model = Inventory
        fields = ['name', 'parent', 'description', 'attrs']

@login_required
def edit_inventory(request, id):

    instance=Inventory.objects.get(id=id)
    args = {}
    args.update(csrf(request))
    args['id'] = id
    args['username'] = auth.get_user(request).username
    args['form'] = InventoryForm(request.POST or None, instance=instance)
    args['back'] = request.get_full_path()
    if request.POST:
        if "cancel" in request.POST:
            return redirect('inventory.views.show_inventory_classes')
        if args['form'].is_valid():
            args['form'].save()
            return redirect('inventory.views.show_inventory_classes')
        else:
            args['error_messages'] = "Вы ввели некорректные данные. Попробуйте ещё раз."
    return render_to_response("edit.html",
                              args)

@login_required
def add_inventory(request, status = None):

    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = InventoryForm(request.POST or None)
    if request.POST:
        if args['form'].is_valid():
            args['form'].save()
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

    return redirect('inventory.views.show_inventory_classes', status=status)

def home_page(request):
    return render_to_response("base.html",
                              {'username': auth.get_user(request).username},
                              context_instance=RequestContext(request))


