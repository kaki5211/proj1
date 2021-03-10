from django.contrib import admin
from django.urls import path, include
from . import views

appmame = 'arikui'
urlpatterns = [
    path('base/', views.BaseView.as_view(), name='base')
]