from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('login/', login, name="login"),
    #path('register/', register, name="register"),
    path('register', register, name='register'), 
    path('logout', logout, name='logout'), 
]