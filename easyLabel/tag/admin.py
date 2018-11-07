from django.contrib import admin

from .models import Picture, Label1


class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'height', 'width', 'imageRelativeUrl', 'label1', 'updated')
    list_filter = ('origin', 'label1', 'updated')
    search_fields = ('name', 'label1', 'origin')
    ordering = ['name']


class Label1Admin(admin.ModelAdmin):
    list_display = ('label',)
    ordering = ('label',)


admin.site.register(Picture, PictureAdmin)
admin.site.register(Label1, Label1Admin)
