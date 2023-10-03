from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    print(request.POST)
    return render(request, 'cadastro.html')
