import requests.exceptions
import os
from django.shortcuts import render
from .forms import CreateUserForm, UploadFile
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .tests import passMatch, passLength, emailValidity, strongPassword,getAddress,updateAddress,updateindex,getindex
from .models import User, UserData
import hashlib as hash
from .ipfsPinata import upload, remove
from requests.exceptions import ConnectionError
from web3 import Web3
from .blockchain import deployCon,store,fetch
from django.contrib.auth.decorators import login_required
ganache = "http://127.0.0.1:8545"

w3 = None

def ganacheConnect():
    global w3
    w3 = Web3(Web3.HTTPProvider(ganache))



# Create your views here.

con = deployCon()

def hashing(str1:str, str2:str)->str:
    res = str1+str2
    result = hash.sha256(str(res).encode("utf-8")).hexdigest()
    return result


def index(request):
    return render(request, "ethereumWeb3App/index.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userkey = hashing(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userView', userkey=userkey)
        else:
            messages.info(request, "Username or password is incorrect or user doesn't exists")

    return render(request, "ethereumWeb3App/login.html")




@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    ganacheConnect()
    if not w3.isConnected():
        return render(request,"ethereumWeb3App/ganache.html")
    var = getAddress()

    address = w3.eth.accounts[var]
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(pass1 + pass2)
        flag1 = emailValidity(email)
        flag2 = passLength(password=pass1)
        flag3 = passMatch(pass1, pass2)
        flag4 = strongPassword(pass1)

        print(flag3)
        if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1:
            messages.success(request, "Account was created for :" + username)
            form.username = username
            form.email = email
            form.password1 = pass1
            form.password2 = pass2
            userKey: str = hashing(username, pass1)
            u = User(username=username,userKey=userKey,pubAddress=address)
            form.save()
            u.save()
            print(var)
            updateAddress()


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

@login_required(login_url='login/')
def userView(request, userkey):
    u = User.objects.get(userKey=userkey)
    addr = u.pubAddress
    ganacheConnect()
    if w3.isConnected():
        balance =w3.fromWei(w3.eth.get_balance(addr),"ether")

        return render(request, "ethereumWeb3App/userview.html", {"userkey": userkey[0:32],
                                                             "address":addr,
                                                             "balance":balance,
                                                             "username":request.user})
    else:
        return render(request,"ethereumWeb3App/ganache.html")


@login_required(login_url='login/')
def Upload(request):
    flag = 0
    if request.method == 'POST':
        flag = 1
        file = request.FILES['document']
        filename = file.name
        fileType = file.content_type
        fileSize = file.size
        print(filename)
        flag = 0
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path = "media/documents/"+filename
            res = upload(path,filename)
            ipfshash = res['rows'][0]['ipfs_pin_hash']
            data = UserData.objects.all()

            for i in data:
                if ipfshash==i.IpfsHash:
                    remove(ipfshash)
                    messages.info(request,"Ownership already exists in blockchain , cannot upload")
                    u = User.objects.get(username=request.user)
                    userk = u.userKey
                    return redirect('userView',userk)
            gateway = "https://gateway.pinata.cloud/ipfs/"
            url = gateway+ipfshash
            user = User.objects.get(username=request.user)
            addr = user.pubAddress
            tx = store(con, address=addr, hash=ipfshash)
            d = UserData(index=getindex(),user=user,AssetName=filename, IpfsUrl=url,TypeOfData=fileType,IpfsHash=ipfshash,UploadTnxHash=tx)
            d.save()
            updateindex()

            messages.info(request, "File has been successfully Uploaded ")
        u = User.objects.get(username=request.user)
        userk = u.userKey

        return redirect('userView',userk)
    else:
        form = UploadFile()
        return render(request, "ethereumWeb3App/uploadFile.html", {'form': form,'flag':flag})

@login_required(login_url='login/')
def history(request):
    u = User.objects.get(username=request.user)
    d = UserData.objects.filter(user=u)
    context = {
        "file": d
    }
    return render(request, "ethereumWeb3App/history.html", context)


def blog(request):

    return render(request, "ethereumWeb3App/blog.html")
