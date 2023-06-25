from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('platos/', plato_list, name="platos"),    
   
]