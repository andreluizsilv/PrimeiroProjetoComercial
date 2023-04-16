from django.urls import path
from .views import Homecadastro, Homepage

urlpatterns = [
    path('', Homepage.as_view()),
    path('cliente_cadastrado/', Homecadastro.as_view()),
]