from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class custome_user_admin(UserAdmin):
    pass
admin.site.register(custom_user,custome_user_admin)
admin.site.register(judge)
admin.site.register(clerk)
admin.site.register(lawyer)
