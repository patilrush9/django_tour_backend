from django.contrib import admin
from tourapp.models import *
# Register your models here.
# class OrderAdmin(admin.ModelAdmin):
# 	pass


admin.site.register(tour)
admin.site.register(gallery)
admin.site.register(enquiry)