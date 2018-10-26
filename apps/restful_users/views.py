from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.

from .models import User

def index(request):
    return render(request, "restful_users/index.html", { "users": User.objects.all() })

def new(request):
    return render(request, "restful_users/new_user.html")

def edit(request, number):
    return render(request, "restful_users/edit_user.html", { "user": User.objects.get(id=number) })

def show(request, number):
    return render(request, "restful_users/show_user.html", { "user": User.objects.get(id=number) })

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        user = User.objects.create()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        id = str(user.id)
        return redirect("/users/"+id)

def destroy(request, number):
    user = User.objects.get(id=number)
    user.delete()
    return redirect("/users")

def update(request, number):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+number+'/edit/')
    else:
        user = User.objects.get(id=number)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    return redirect("/users/"+number+"/edit/")