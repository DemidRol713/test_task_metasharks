from django.contrib import admin

from .models import BrandAuto, ModelAuto, Color


class BrandAutoAdmin(admin.ModelAdmin):
    list_display = ['name']


class ModelAutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(BrandAuto, BrandAutoAdmin)
admin.site.register(ModelAuto, ModelAutoAdmin)
admin.site.register(Color, ColorAdmin)