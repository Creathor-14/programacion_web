from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('principales/', principal_list, name="principales"),    
    path('principales/<str:principal_id>', principal_delete, name="principal-delete"),
    path('principales/detail/<str:principal_id>', principal_detail, name="principal-detail"),
    path('principales/edit/<str:principal_id>', principal_update, name="principal-edit"),
    path('principales/new/', principal_new, name="principal-new"),

    path('postres/', postre_list, name="postres"),    
    path('postres/<str:postre_id>', postre_delete, name="postre-delete"),
    path('postres/detail/<str:postre_id>', postre_detail, name="postre-detail"),
    path('postres/edit/<str:postre_id>', postre_update, name="postre-edit"),
    path('postres/new/', postre_new, name="postre-new"),

    path('bebestibles/', bebestible_list, name="bebestibles"),    
    path('bebestibles/<str:bebestible_id>', bebestible_delete, name="bebestible-delete"),
    path('bebestibles/detail/<str:bebestible_id>', bebestible_detail, name="bebestible-detail"),
    path('bebestibles/edit/<str:bebestible_id>', bebestible_update, name="bebestible-edit"),
    path('bebestibles/new/', bebestible_new, name="bebestible-new"),
]