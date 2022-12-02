from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AddTable
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationform
from . forms import UserLoginform

# Create your views here.
def mainhome(request):
    return render(request, "mainhome.html")


def error(request):
    return render(request, "error.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationform()
    return render(request, "login.html",{'form':form})

def login(request):
    if request.method == "POST":
        form = UserLoginform(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = UserLoginform
    return render(request, "login.html",{'form':form})


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def menu(request):
    return render(request, "menu.html")


def table(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        branch = request.POST['branch']
        people = request.POST['people']
        new_table = AddTable(name=name, email=email, date=date, time=time, branch=branch, people=people)
        new_table.save()
    return render(request, 'table.html', {})


def about(request):
    return render(request, "about.html")


def profile(request):
    return render(request, "profile.html")
