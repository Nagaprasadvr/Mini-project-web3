from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "ethereumWeb3App/login.html")


def registerPage(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for :" + user)
            return redirect('login')

    return render(request, "ethereumWeb3App/register.html", context)


def home(request):
    return render(request, "ethereumWeb3App/index.html")


def blog(request):
    return render(request, "ethereumWeb3App/blog.html")