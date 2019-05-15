from django.contrib import admin
from .models import Location, Category, Image

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
