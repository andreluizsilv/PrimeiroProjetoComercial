from django.shortcuts import render
from .models import Cliente
# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

# view - url html

def homecadastro(request):
    context = {}
    clientes_cadastrado = Cliente.objects.all()
    context['clientes_cadastrado'] = clientes_cadastrado
    return render(request, "homecadastro.html", context)