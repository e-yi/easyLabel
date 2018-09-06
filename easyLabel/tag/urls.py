from django.urls import path
from . import views

urlpatterns = [
    path('pictures/list/',
         views.picture_list),
    path('pictures/<int:pk>',
         views.picture_detail),
    path('tags/',
         views.label1_list),
]
