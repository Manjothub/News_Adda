from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('',HOME, name= 'homepage')
]