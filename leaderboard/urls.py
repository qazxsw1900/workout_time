from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_time/', views.addTime, name='addTime'),
    path('result/', views.result, name='result'),
]