from django.contrib import admin


from .models import User,UserData,Document,AccIndex

admin.site.register(User)
admin.site.register(UserData)
admin.site.register(Document)
admin.site.register(AccIndex)

