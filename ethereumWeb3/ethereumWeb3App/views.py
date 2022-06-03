from django.shortcuts import render
from .forms import CreateUserForm,UploadFile
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .tests import passMatch,passLength,emailValidity,strongPassword
from .models import User
import hashlib as hash
# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")



def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userView', username=(username[0].upper()+username[1:]))
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
    flag4 = 0

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
        flag4 = strongPassword(pass1)

        print(flag3)
        if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1:
            messages.success(request, "Account was created for :" + username)
            form.username = username
            form.email = email
            form.password1 = pass1
            form.password2 = pass2
            form.save()
            hashVal: str = hash.sha256(str(username+pass1).encode("utf-8")).hexdigest()
            utmp = User(userKey=hashVal, username=username)
            utmp.save()

            return redirect('login')
        elif flag1 == 0:
            messages.info(request, "Invalid email")
        elif flag2 == 0:
            messages.info(request, "Password length is too short")
        elif flag3 == 0:
            messages.info(request, "Passwords don't match")
        elif flag4 == 0:
            messages.info(request, "Weak password - Include numbers , Uppercase and special characters in password")

    return render(request, "ethereumWeb3App/register.html", {})


def home(request):
    return render(request, "ethereumWeb3App/index.html")


def userView(request, username):
    return render(request,"ethereumWeb3App/userview.html",  {"username": username})


def Upload(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadFile()
        return render(request, "ethereumWeb3App/uploadFile.html", {'form': form})


def blog(request):
    return render(request, "ethereumWeb3App/blog.html")