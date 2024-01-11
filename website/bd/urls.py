from django.urls import path
from . import views

urlpatterns = [
    path('', views.zapis, name='zapis'),
    path('create', views.create, name ='create'),
    path('vrach/', views.vrachi, name='vrach'),
]
