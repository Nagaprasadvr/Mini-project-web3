from django.contrib import admin


from .models import User,UserData,Document

admin.site.register(User)
admin.site.register(UserData)
admin.site.register(Document)

