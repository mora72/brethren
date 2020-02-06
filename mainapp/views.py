from django.shortcuts import render, get_object_or_404
from .models import Local, Irmao
from .forms import LocalForm


def main_menu(request):
    search = request.GET.get('search')  # usa o name="search" informado no input do locais.html
    filteruf = request.GET.get('filteruf')
    if search:
        lista_locais = Local.objects.filter(nomelocal__icontains=search)
        filteruf = str(None)
    elif (not filteruf) or filteruf == '*':
        lista_locais = Local.objects.all().order_by('criado')
    else:
        lista_locais = Local.objects.filter(uf=filteruf)
    return render(request, 'mainapp/locais.html', {'listalocais': lista_locais, 'filterufatual': filteruf})


def irmaos_view(request):
    lista_irmaos = Irmao.objects.all().order_by('criado')
    return render(request, 'mainapp/irmaos.html', {'listairmaos': lista_irmaos})


def local_view(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    form = LocalForm(instance=local)
    return render(request, 'mainapp/localview.html', {'form': form, 'local': local})
