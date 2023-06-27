from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('principales/', principal_list, name="principales"),    
    path('principales/<str:principal_id>', principal_delete, name="principal-delete"),
    path('principales/detail/<str:principal_id>', principal_detail, name="principal-detail"),
    path('principales/edit/<str:principal_id>', principal_update, name="principal-edit"),
    path('principales/new/', principal_new, name="principal-new"),
]