from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path,include
from . import views
# Create your views here.
def home(request):
    # return HttpResponse("hello I am working")
    return render(request, "authentication/signin.html")

def signup(request):
    return render(request, "authentication/signup.html")

# def signin(request):
#     return render(request, "authentication/sign_in.html")

def signout(request):
    pass
