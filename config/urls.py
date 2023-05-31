from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    # path('login', views.login, name='login'),
    # path('logout/', views.signup, name='logout'),
    path('contact/', views.Contact, name='contact'),
    path('view/<int:id>', views.view, name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
