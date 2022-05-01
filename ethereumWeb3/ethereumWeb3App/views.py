from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .tests import passMatch,passLength,emailValidity
# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "ethereumWeb3App/login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    flag1 = 0
    flag2 = 0
    flag3 = 0

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(pass1+pass2)
        flag1 = emailValidity(email)
        flag2 = passLength(password=pass1)
        flag3 = passMatch(pass1,pass2)
        print(flag3)
        if flag1 == 1 and flag2 == 1 and flag3 == 1:
            messages.success(request, "Account was created for :" + username)
            form.username = username
            form.email = email
            form.password1 = pass1
            form.password2 = pass2
            form.save()
            return redirect('login')
        elif flag1 == 0:
            messages.info(request, "Invalid email")
        elif flag2 == 0:
            messages.info(request, "Password length is too short")
        elif flag3 == 0:
            messages.info(request, "Passwords don't match")

    return render(request, "ethereumWeb3App/register.html", {})


def home(request):
    return render(request, "ethereumWeb3App/index.html")


def blog(request):
    return render(request, "ethereumWeb3App/blog.html")