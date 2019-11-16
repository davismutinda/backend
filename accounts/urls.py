from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from .views import *
urlpatterns = [
        path('login/',login), 
]