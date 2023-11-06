from django.shortcuts import render

# Create your views here.
def gerenciar_clientes(request):
    return render(request, 'gerenciar_clientes.html')