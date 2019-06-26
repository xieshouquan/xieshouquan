from django.contrib import admin

# Register your models here.
from hypermarket.models import CmmodityType,Cmmodity

admin.site.register(CmmodityType)
admin.site.register(Cmmodity)