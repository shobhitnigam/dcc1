from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from . import views

from django.contrib import admin

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('tologin',views.tologin,name='tologin'),
    path('login',views.login,name='login'),
    path('admin', admin.site.urls)
]