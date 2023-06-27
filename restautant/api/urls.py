from django.urls import path, include
from rest_framework import routers
from api import views

from .views import *



router = routers.DefaultRouter()
router.register(r'formularios',views.ContactoListCreateView)


urlpatterns=[
    path('',include(router.urls)),
    path('principales/', principal_list),
    path('principales/<str:principal_id>', principal_detail),
    #path('postres/', postres_list),
    path('postres/', postre_list),
    path('postres/<str:postre_id>', postre_detail),
    #path('bebestibles/', bebestibles_list),
    path('bebestibles/', bebestible_list),
    path('bebestibles/<str:bebestible_id>', bebestible_detail),
    path('contacto/contact', ContactoListCreateView.as_view({'get': 'list', 'post': 'create'}), name='contact_list_create'),
]
