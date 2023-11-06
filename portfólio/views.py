from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.db.models import Value

def gerenciar_clientes(request):
    clientes = User.objects.filter(is_staff=False)
    
    nome_completo = request.GET.get('nome')
    email = request.GET.get('email')

    if email:
        clientes = clientes.filter(email__contains = email)

    if nome_completo:
        clientes = clientes.annotate(full_name=Concat('first_name', Value(' '), 'last_name')).filter(full_name__contains=nome_completo)


    print(f'{nome_completo} - {email}')
    return render(request, 'gerenciar_clientes.html', {'clientes': clientes})