# coding=utf-8
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.context_processors import csrf

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #remember_me = request.POST.get('remember_me', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            else:
                args['login_error'] = 'Пользователь не активен'
                return render_to_response("login.html",
                                          args,
                                          context_instance=RequestContext(request))
        else:
            args['login_error'] = 'Пользователь не найден, или пароль не верен'
            return render_to_response("login.html",
                                      args,
                                      context_instance=RequestContext(request))
    else:
        return render_to_response("login.html",
                                      context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return redirect('/')


class RegisterForm(UserCreationForm):

    username = forms.CharField(label=_("Логин"), max_length=30, error_messages={'required': 'Пожалуйста, введите Ваш логин.'})
    password1 = forms.CharField(label=_("Пароль"), max_length=30)
    password2 = forms.CharField(label=_("Повторите пароль"), max_length=30)
    email = forms.EmailField(label = _("Email"))
    first_name = forms.CharField(label = _("Имя"), required=False)
    last_name = forms.CharField(label = _("Фамилия"), required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        #user.username = self.cleaned_data.get("username")
        #user.password = self.cleaned_data.get("password1")
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        if commit:
            user.save()
        return user


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegisterForm()
    if request.POST:
        newuser_form = RegisterForm(request.POST)
        if newuser_form.is_valid():
            # Save new user into DB
            newuser_form.save()
            # Authenticate user right here
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password2'])
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response("register.html",
                              args,
                              context_instance=RequestContext(request))