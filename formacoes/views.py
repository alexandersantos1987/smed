from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Formacao

# Create your views here.
def index(request):
    return render(request, 'formacoes/index.html')

def ativas(request):
    formacoes = Formacao.objects.all().order_by('data').filter(ativa=True)
    return render(request, 'formacoes/formacoes.html', {'formacoes': formacoes, 'ativa': True})

def passadas(request):
    formacoes = Formacao.objects.all().order_by('data').filter(ativa=False)
    return render(request, 'formacoes/formacoes.html', {'formacoes': formacoes, 'ativa': False})

def formacoes(request):
    formacoes = serialize('json', Formacao.objects.all())
    return HttpResponse(formacoes, content_type="application/json")