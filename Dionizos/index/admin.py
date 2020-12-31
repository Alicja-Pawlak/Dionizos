from django.contrib import admin
from index.models import Wines

# Register your models here.

class WinesAdmin(admin.ModelAdmin):
    list_display=("name","price","color","taste","descriptions","picture",)

admin.site.register(Wines,WinesAdmin)

