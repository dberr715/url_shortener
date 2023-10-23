from django.contrib import admin
from .models import UrlData
from .models import UserData

# Register your models here.
admin.site.register(UrlData)
admin.site.register(UserData)
