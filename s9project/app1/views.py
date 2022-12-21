from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from pymongo import MongoClient

from .models import AddTable

client=MongoClient("mongodb://127.0.0.1:27017/")
db=client["SDP"]
coll=db.stu
coll2=db.tab
# Create your views here.
def mainhome(request):
    return render(request, "mainhome.html")



def error(request):
    return render(request, "error.html")


def login(request):
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def menu(request):
    return render(request, "menu.html")

def table(request):
    return render(request, 'table.html')

def about(request):
    return render(request, "about.html")
def addtocart(request):
    return render(request, "addtocart.html")

def getres(request):
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        email_id=request.POST.get('email_id')
        pswd=request.POST.get('pswd')
        l, u, p, d = 0, 0, 0, 0
        s = pswd
        if (len(s) >= 6):
            for i in s:

                # counting lowercase alphabets
                if (i.islower()):
                    l += 1

                    # counting uppercase alphabets
                if (i.isupper()):
                    u += 1

                    # counting digits
                if (i.isdigit()):
                    d += 1

                    # counting the mentioned special characters
                if (i == '@' or i == '$' or i == '_'):
                    p += 1
        if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
            db.coll.insert_one({'user_name': user_name, 'email_id': email_id, 'pswd': pswd})
            return render(request, "login.html")
        else:
            messages.error(request, "Invalid Password!!!  Register Again!!!")
            return render(request, "login.html")


def checkuser(request):
    if request.method=='POST':
        l_username=request.POST.get('l_username')
        l_pswd=request.POST.get('l_pswd')

        c=db.coll.find_one({'user_name':l_username})

        if c['user_name']==l_username and c['pswd']==l_pswd:
             return render(request,"home.html")
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def gettableres(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sdate = request.POST.get('sdate')
        stime = request.POST.get('stime')
        branch = request.POST.get('branch')
        people = request.POST.get('people')
        db.coll2.insert_one(
            {'name': name, 'email': email, 'sdate': sdate, 'stime': stime, 'branch': branch, 'people': people})
        return render(request, "home.html")
    return render(request, "home.html")
def addtocart2(request):
    return render(request, "addtocart2.html")
def payment(request):
    return render(request, "payment.html")
