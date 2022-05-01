from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def loginPage(request):
    return render(request,"ethereumWeb3App/login.html")


def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "ethereumWeb3App/register.html", context)


def home(request):
    return render(request,"ethereumWeb3App/index.html")

def blog(request):
    return render(request, "ethereumWeb3App/blog.html")