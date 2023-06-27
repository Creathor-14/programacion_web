from django.urls import path, include
from rest_framework import routers
from api import views

from .views import *



router = routers.DefaultRouter()
#router.register(r'principales',views.PrincipalViewSet)
#router.register(r'postres',views.PostreViewSet)
#router.register(r'bebestibles',views.BebestibleViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('principales/', principal_list),
    path('principales/<str:principal_id>', principal_detail),
    #path('postres/', postres_list),
    #path('bebestibles/', bebestibles_list),
    path('contacto/contact', ContactoListCreateView.as_view({'get': 'list', 'post': 'create'}), name='contact_list_create'),
]
