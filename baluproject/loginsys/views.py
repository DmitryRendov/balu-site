# coding=utf-8
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
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
                args['login_error'] = 'Пользователь не найден'
                return render_to_response("login.html",
                                          args,
                                          context_instance=RequestContext(request))
    else:
        return render_to_response("login.html",
                                      context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            # Save new user into DB
            newuser_form.save()
            # Authentificate user right here
            newuser = auth.authenticate(username=newuser_form.clean_username(),password=newuser_form.clean_password2())
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response("register.html",
                              args,
                              context_instance=RequestContext(request))