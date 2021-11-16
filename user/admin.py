from django.contrib import admin
from user.models import User
# Register your models here.
# class OrderAdmin(admin.ModelAdmin):
# 	pass


admin.site.register(User)