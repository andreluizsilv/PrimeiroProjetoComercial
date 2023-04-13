from django.urls import path
from .views import homepage, homecadastro

urlpatterns = [
    path('', homepage),
    path('cliente_cadastrado/', homecadastro),
]