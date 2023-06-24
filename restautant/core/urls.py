from django.urls import path
from .views import * 

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('historia/', historia, name='historia'),
    path('chistes/', chistes, name='chistes'),
]
