from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('index.html', views.shop),
    path('counter', views.counter),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('shop.html', views.shop),
]