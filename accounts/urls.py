from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_views

urlpatterns=[
    path('token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    path('data/', GetUser.as_view(), name='user-data'),
    
]