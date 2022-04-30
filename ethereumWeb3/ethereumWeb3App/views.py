from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def home(request):
    return render(request,"ethereumWeb3App/index.html")