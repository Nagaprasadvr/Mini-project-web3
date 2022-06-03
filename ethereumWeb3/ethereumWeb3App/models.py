from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    userKey = models.CharField(max_length=100, primary_key=True, default="1234")

    def __str__(self):
        return self.username


class UserData(models.Model):
    index = models.IntegerField(serialize=True,default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    TypeOfData = models.CharField(max_length=100, null=True, blank=True)
    IpfsHash = models.CharField(primary_key=True,max_length=100, unique=True, null=False , default="")
    TimeStamp = models.DateTimeField(auto_now_add=False,unique=True, null=True, blank=True)
    UploadTnxHash = models.CharField(max_length=100, null=True,unique=True, blank=True)

    def __str__(self):
        return self.IpfsHash


class Document(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploadTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
