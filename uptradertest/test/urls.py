from django.contrib import admin
from django.urls import path, include

from .views import test, GetMenuItem

urlpatterns = [
    path('', test, name='main_page'),
    path('menu_item/<str:slug>', GetMenuItem.as_view(), name='menu_item')
]