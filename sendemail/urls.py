from django.contrib import admin
from django.urls import path

from .views import portfolio_view  #contactView, successView

urlpatterns = [
    path("contact/", portfolio_view, name="contact"),
    
    # path("contact/", contactView, name="contact"),
    # path("success/", successView, name="success"),
]