from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)  # Connect to the index method in views.py
]
