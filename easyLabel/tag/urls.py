from django.urls import path
from . import views

urlpatterns = [
    path('pictures/',
         views.picture_info),
    path('pictures/list/',
         views.picture_list),
    path('pictures/any/',
         views.picture_random),
    path('pictures/<int:pk>/',
         views.picture_detail),
    path('tags/',
         views.label1_list),
]
