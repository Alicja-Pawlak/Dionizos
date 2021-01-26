from django.contrib import admin
from index.models import Wine, Comment, Taste, Color

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    list_display=("name","price","color","taste","descriptions","image",)

class CommentAdmin(admin.ModelAdmin):
    list_display=("nickname", "description",)

class TasteAdmin(admin.ModelAdmin):
    list_display=("taste",)

class ColorAdmin(admin.ModelAdmin):
    list_display=("color",)


admin.site.register(Wine,WineAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Taste,TasteAdmin)
admin.site.register(Color,ColorAdmin)


