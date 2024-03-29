from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('login/', views.auth, name='auth'),
    path('logout/', views.loggout, name='logout'),
]