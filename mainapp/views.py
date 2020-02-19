from django.shortcuts import render, get_object_or_404, redirect
from .models import Local, Irmao, Uf, Distancia
from .forms import LocalForm, LocalFormEdit, IrmaoForm, IrmaoFormEdit
from .modulosbrethren import calcula_distancia
from django.contrib import messages
from django.contrib.auth import get_user_model


def local_list(request):
    search = request.GET.get('search')  # usa o name="search" informado no input do locais.html
    filteruf = request.GET.get('filteruf')
    if type(filteruf) is str:
        filteruf = int(filteruf)
    base_ufs = Uf.objects.all()
    lista_locais = Local.objects.all().order_by('nomelocal')
    if search:
        lista_locais = lista_locais.filter(nomelocal__icontains=search).order_by('nomelocal')
    if filteruf:
        if filteruf != 0:
            lista_locais = lista_locais.filter(uf=filteruf).order_by('nomelocal')
    return render(request, 'mainapp/locais.html', {'listalocais': lista_locais, 'filterufatual': filteruf,
                                                   'listaufs': base_ufs})


def local_view(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    form = LocalForm(instance=local)
    return render(request, 'mainapp/localview.html', {'form': form, 'local': local})


def local_delete(request, idlocal):
    local = get_object_or_404(Local, pk=idlocal)
    local.delete()

    messages.info(request, f'Localidade "{local.nomelocal}" removida com Sucesso !')

    return redirect('/')


def local_new(request):
    usuariomodel = get_user_model()
    usuariodef = get_object_or_404(usuariomodel, pk=1)
    if request.method == 'POST':
        form = LocalFormEdit(request.POST)
        if form.is_valid():
            local = form.save(commit=False)
            local.usuario = usuariodef
            local.save()
            return redirect('/')
    else:
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


def irmaos_list(request):
    searchirmao = request.GET.get('searchirmao')  # usa o name="search" informado no input do irmaos.html
    filterstatus = request.GET.get('filterstatus')
    filterlocal = request.GET.get('filterlocal')
    lista_irmaos = Irmao.objects.all().order_by('nome')

    if type(filterlocal) is str:
        filterlocal = int(filterlocal)

    if searchirmao:
        lista_irmaos = lista_irmaos.filter(nome__icontains=searchirmao)

    if filterstatus and filterstatus != '*':
        lista_irmaos = lista_irmaos.filter(status=filterstatus)

    if filterlocal and filterlocal != 0:
        lista_irmaos = lista_irmaos.filter(local=filterlocal)

    lista_locais = Local.objects.all().order_by('nomelocal')
    return render(request, 'mainapp/irmaos.html', {'listairmaos': lista_irmaos, 'filterstatusatual': filterstatus,
                                                   'listalocais': lista_locais, 'filterlocalatual': filterlocal})


def irmaos_view(request, idirmao):
    irmao = get_object_or_404(Irmao, pk=idirmao)
    form = IrmaoForm(instance=irmao)
    return render(request, 'mainapp/irmaoview.html', {'form': form, 'irmao': irmao})


def irmao_delete(request, idirmao):
    irmao = get_object_or_404(Irmao, pk=idirmao)
    irmao.delete()

    messages.info(request, f'Irmão "{irmao.nome}" removido com Sucesso !')

    return redirect('/irmaos/')


def irmao_new(request):
    usuariomodel = get_user_model()
    usuariodef = get_object_or_404(usuariomodel, pk=1)
    if request.method == 'POST':
        form = IrmaoFormEdit(request.POST, request.FILES)
        if form.is_valid():
            irmao = form.save(commit=False)
            irmao.usuario = usuariodef
            irmao.save()
            return redirect('/irmaos/')
    else:
        form = IrmaoFormEdit()
        return render(request, 'mainapp/irmaonew.html', {'form': form})


def irmao_edit(request, idirmao):
    irmao = get_object_or_404(Irmao, pk=idirmao)
    form = IrmaoFormEdit(instance=irmao)

    if request.method == 'POST':
        form = IrmaoFormEdit(request.POST, request.FILES, instance=irmao)

        if form.is_valid():
            print(irmao.imagefoto)
            irmao.save()
            print(irmao.imagefoto)
            return redirect('/irmaos/')
        else:
            return render(request, 'mainapp/irmaoedit.html', {'form': form, 'irmao': irmao})
    else:
        return render(request, 'mainapp/irmaoedit.html', {'form': form, 'irmao': irmao})


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
