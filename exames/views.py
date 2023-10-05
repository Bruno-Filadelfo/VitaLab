from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def solicitar_exames(request):
    if not (request.user.is_authenticated):
        return  HttpResponse("Você não pode acessar aqui")
    return HttpResponse('Estou aqui')

