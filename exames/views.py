from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames

@login_required
def solicitar_exames(request):
    if request.method == "GET":
       tipos_exames = TiposExames.objects.all()
       return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        # calcular preço dos dados disponíveis 
        preco_total = 0
        for i in solicitacao_exames:
            preco_total += i.preco
            
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
