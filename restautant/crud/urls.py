from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('platos/', plato_list, name="platos"),    
    path('platos/<str:plato_id>', plato_delete, name="plato-delete"),
    path('platos/detail/<str:plato_id>', plato_detail, name="plato-detail"),
    path('platos/edit/<str:plato_id>', plato_update, name="plato-edit"),
    path('platos/new/', plato_new, name="plato-new"),
]