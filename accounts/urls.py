from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('signup',views.signup, name='signup'),
]
