from django.urls import path
from . import views

urlpatterns = [
    path('settings/<int:id>/', views.update_profile, name='update_profile'),
]
