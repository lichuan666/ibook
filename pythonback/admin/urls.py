from django.urls import path

from . import views

# app_name = 'admin'
urlpatterns = [
    path('login/', views.login, name="login"), 
    path('setseat/', views.setseat, name="setseat"), 
    path('statistic/', views.statistic, name="statistic"), 
    path('setroom/', views.setroom, name="setroom"), 
]
