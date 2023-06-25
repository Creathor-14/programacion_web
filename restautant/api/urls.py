from django.urls import path, include
from rest_framework import routers
from api import views

from .views import ContactoListCreateView



router = routers.DefaultRouter()
router.register(r'platos',views.PlatoViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('contacto/contact', ContactoListCreateView.as_view({'get': 'list', 'post': 'create'}), name='contact_list_create'),
]
