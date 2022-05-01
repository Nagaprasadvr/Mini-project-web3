from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def loginPage(request):
    return render(request,"ethereumWeb3App/login.html")


def registerPage(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for :" + user )
            return redirect('login')

    return render(request, "ethereumWeb3App/register.html", context)


def home(request):
    return render(request,"ethereumWeb3App/index.html")

def blog(request):
    return render(request, "ethereumWeb3App/blog.html")