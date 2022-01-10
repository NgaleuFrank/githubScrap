from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register', views.register, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('images', views.images, name='images'),
]
