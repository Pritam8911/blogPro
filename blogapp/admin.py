from django.contrib import admin
from .models import *

# Register your models here.
class DirectorAdmin(admin.ModelAdmin):
    list_display=['title','director']



admin.site.register(NewArrival,DirectorAdmin)
admin.site.register(Director)
admin.site.register(Cast)