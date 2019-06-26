from django.contrib import admin

# Register your models here.
from consumer.models import MyUser

admin.site.register(MyUser)

