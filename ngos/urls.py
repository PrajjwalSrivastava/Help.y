from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('create',views.create,name='create'),
    path('children',views.children,name='children'),
    path('women',views.women,name='women'),
    path('elderly',views.elderly,name='elderly'),
    path('cancer',views.cancer,name='cancer'),
    path('homeless',views.homeless,name='homeless'),
    path('hunger',views.hunger,name='hunger'),
    path('differently_abled',views.differently_abled,name='differently_abled'),
    path('search',views.search,name='search'),
    path('<registration_number>',views.detail,name='detail'),
]
