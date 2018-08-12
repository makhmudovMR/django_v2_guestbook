from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'sign/', views.sign, name='sign'),
]