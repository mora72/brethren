from django.shortcuts import render
from .models import Local, Irmao


def main_menu(request):
    lista_locais = Local.objects.all().order_by('criado')
    return render(request, 'mainapp/locais.html', {'listalocais': lista_locais})


def irmaos_view(request):
    lista_irmaos = Irmao.objects.all().order_by('criado')
    return render(request, 'mainapp/irmaos.html', {'listairmaos': lista_irmaos})
