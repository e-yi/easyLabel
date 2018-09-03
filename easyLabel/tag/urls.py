from django.urls import path
from . import views

urlpatterns = [
    path('pictures/',
         views.picture_list),
    path('pictures/<int:pk>',
         views.picture_detail)
]
