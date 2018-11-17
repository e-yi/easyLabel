from django.urls import path
from . import views

urlpatterns = [
    path('pictures/',
         views.picture_info),
    path('pictures/csv',
         views.output_download),
    path('pictures/list/',
         views.picture_list),
    path('pictures/any/',
         views.picture_random),
    path('pictures/<int:pk>/',
         views.picture_detail),
    path('pictures/review/<label1>',
         views.picture_review),
    path('picture/review/<label1>/<int:step>',
         views.picture_review),
    path('tags/',
         views.label1_list),
]
