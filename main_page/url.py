from django.urls import path
from . import views

urlpatterns = [
    path('mainPage/', views.main_page, name='mainPage'),
]
