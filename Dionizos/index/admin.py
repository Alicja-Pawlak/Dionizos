from django.contrib import admin
from index.models import Wine, Comment, Taste, Color, WineImage

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    list_display=("name","price","color","taste","descriptions","image",)

class CommentAdmin(admin.ModelAdmin):
    list_display=("nickname", "description",)

class TasteAdmin(admin.ModelAdmin):
    list_display=("taste",)

class ColorAdmin(admin.ModelAdmin):
    list_display=("color",)

class WineImageAdmin(admin.StackedInline):
    model = WineImage

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    inlines = [WineImageAdmin] 

    class Meta:
       model = Wine

@admin.register(WineImage)
class WineImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment,CommentAdmin)
admin.site.register(Taste,TasteAdmin)
admin.site.register(Color,ColorAdmin)


