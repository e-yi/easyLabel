from django.contrib import admin

from .models import Picture, Label1


class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'size', 'image', 'label1')
    list_filter = ('origin', 'label1')
    search_fields = ('name', 'label1', 'origin')
    ordering = ['name']


class Label1Admin(admin.ModelAdmin):
    list_display = ('label1',)
    ordering = ('label1',)


admin.site.register(Picture, PictureAdmin)
admin.site.register(Label1, Label1Admin)
