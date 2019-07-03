from django.contrib import admin

# Register your models here.
from consumer.models import MyUser, UserCmmodity, UserPin

admin.site.register(MyUser)
admin.site.register(UserCmmodity)
admin.site.register(UserPin)

