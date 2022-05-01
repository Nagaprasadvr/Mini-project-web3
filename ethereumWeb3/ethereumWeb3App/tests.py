from django.test import TestCase

# Create your tests here.


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

