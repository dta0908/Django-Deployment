from django.conf.urls import url
from django.urls import path
from hello_app import views

urlpatterns = [
    path('', views.index, name = 'index')
]
