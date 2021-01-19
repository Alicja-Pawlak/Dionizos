from django.contrib import admin
from index.models import Wines, Comments

# Register your models here.

class WinesAdmin(admin.ModelAdmin):
    list_display=("name","price","color","taste","descriptions","image",)


class CommentsAdmin(admin.ModelAdmin):
    list_display=("nickname", "description",)

admin.site.register(Wines,WinesAdmin)
admin.site.register(Comments,CommentsAdmin)


