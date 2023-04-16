from django.shortcuts import render
from .models import Cliente
from django.views.generic import TemplateView, ListView


# Create your views here.
#def homepage(request):
    #return render(request, "homepage.html")

# view - url html
class Homepage(TemplateView):
    template_name = "homepage.html"
#def homecadastro(request):
#    context = {}
#    clientes_cadastrado = Cliente.objects.all()
#    context['clientes_cadastrado'] = clientes_cadastrado
#    return render(request, "homecadastro.html", context)

class Homecadastro(ListView):
    template_name = "homecadastro.html"
    model = Cliente