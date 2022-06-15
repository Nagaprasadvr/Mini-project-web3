from django.test import TestCase
from django.contrib import messages
import json
from .models import AccIndex
# Create your tests here.

var = 1
def passLength(password: str):
    if len(password) >= 10:
        return True
    else:
        return False


def passMatch(password1: str, password2:str):
    if password1 == password2:
        return True
    else:
        return False


def emailValidity(email: str):
    flag = 0
    if "@" not in email:
        flag = 1
    elif ".com" not in email:
        flag = 1

    if flag == 1:
        return False
    else:
        return True


def strongPassword(password: str):
    flag1 = 0
    flag2 = 0
    flag3 = 0

    for i in password:
        if i.isupper():
            flag1 = 1
        elif i.isdigit():
            flag2 = 1
        elif i == "!" or  i == "@" or  i == "#" or  i == "$" or  i == "%" or  i == "&" or  i == "(" or i == ")" or i == "/" or i == "[" or i == "]" :
            flag3 = 1

    if flag1 == 1 and flag2 == 1 and flag3 == 1:
        return True
    else:
        return False


def getAddress():
    i = AccIndex()
    file = open("store.json", 'r')
    jsonObj = json.load(file)
    file.close()
    return jsonObj['index']



def updateAddress():
    file = open("store.json", "r")
    jsonObj = json.load(file)
    jsonObj['index'] += 1
    file.close()
    file = open("store.json", "w")
    json.dump(jsonObj,file)
    file.close()
    return jsonObj['index']








