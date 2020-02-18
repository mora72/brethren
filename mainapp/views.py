from django.shortcuts import render, get_object_or_404, redirect
from .models import Local, Irmao, Uf, Distancia
from .forms import LocalForm, LocalFormEdit, IrmaoForm
from .modulosbrethren import calcula_distancia
from django.contrib import messages
from django.contrib.auth import get_user_model


def main_menu(request):
    search = request.GET.get('search')  # usa o name="search" informado no input do locais.html
    filteruf = request.GET.get('filteruf')
    if type(filteruf) is str:
        filteruf = int(filteruf)
    base_ufs = Uf.objects.all()
    lista_locais = []
    if search:
        lista_locais = Local.objects.filter(nomelocal__icontains=search)
        filteruf = str(None)
    elif (not filteruf) or filteruf == 0:
        if filteruf != 'undefined':
            lista_locais = Local.objects.all().order_by('criado')
    else:
        if filteruf != 'undefined':
            lista_locais = Local.objects.filter(uf=filteruf)
    return render(request, 'mainapp/locais.html', {'listalocais': lista_locais, 'filterufatual': filteruf,
                                                   'listaufs': base_ufs})


def local_view(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    form = LocalForm(instance=local)
    return render(request, 'mainapp/localview.html', {'form': form, 'local': local})


def irmaos_view(request):
    searchirmao = request.GET.get('searchirmao')  # usa o name="search" informado no input do irmaos.html
    filterstatus = request.GET.get('filterstatus')
    if searchirmao:
        lista_irmaos = Irmao.objects.filter(nome__icontains=searchirmao)
        filterstatus = str(None)
    elif (not filterstatus) or filterstatus == '*':
        lista_irmaos = Irmao.objects.all().order_by('criado')
    else:
        lista_irmaos = Irmao.objects.filter(status=filterstatus)
    return render(request, 'mainapp/irmaos.html', {'listairmaos': lista_irmaos, 'filterstatusatual': filterstatus})


def irmaos_id_view(request, idirmao):
    irmao = get_object_or_404(Irmao, pk=idirmao)
    form = IrmaoForm(instance=irmao)
    return render(request, 'mainapp/irmaoview.html', {'form': form, 'irmao': irmao})


def distancias(request):
    local_interesse = request.GET.get('searchlocalinteresse')  # usa o local informado no input do distancias.html
    lista_distancias = []
    if local_interesse:
        lista_distancias = calcula_distancia(local_interesse.strip().upper())
    return render(request, 'mainapp/distancias.html', {'listadistancias': lista_distancias,
                                                       'localinteresse': local_interesse})


def teste():
    new_uf = Uf(id=1)
    new_distancia = Distancia(origem='origemteste', cidade_destino='cidadeteste', uf_destino=new_uf,
                              distancia=10)

    new_distancia.save()


def local_delete(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    local.delete()

    messages.info(request, f'Localidade "{local.nomelocal}" removida com Sucesso !')

    return redirect('/')


def local_new(request):
    print('z', request.method)
    usuariomodel = get_user_model()
    usuariodef = get_object_or_404(usuariomodel, pk=1)
    if request.method == 'POST':
        form = LocalFormEdit(request.POST)

        print('a', form.is_valid())
        if form.is_valid():
            print('1')
            local = form.save(commit=False)
            print('2')
            local.usuario = usuariodef
            print('3')
            local.save()
            print('4')
            return redirect('/')
        else:
            print('b', form.errors)
    else:
        print('c', 'aqui')
        form = LocalFormEdit()
        return render(request, 'mainapp/localnew.html', {'form': form})


def local_edit(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    form = LocalFormEdit(instance=local)

    if request.method == 'POST':
        form = LocalFormEdit(request.POST, instance=local)

        if form.is_valid():
            local.save()
            return redirect('/')
        else:
            return render(request, 'mainapp/localedit.html', {'form': form, 'local': local})
    else:
        return render(request, 'mainapp/localedit.html', {'form': form, 'local': local})
