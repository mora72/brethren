from ..models import Local, Distancia
from operator import itemgetter
from ..distcalcmodule import *


def get_distances(origem, cidade_destino, uf_destino, lista_dist_atuais):
    dist = 0
    for x in lista_dist_atuais:
        if x.origem == origem and x.cidade_destino == cidade_destino and x.uf_destino == uf_destino:
            dist = x.distancia
            break
    return dist


def calcula_distancia(local_busca):
    lista_locais = Local.objects.all()
    #  print(f'local busca dentro: {local_busca}')
    #  print(f'UF busca dentro: {uf_busca}')
    lista_dist_calc = {}
    lista_dist_atuais = Distancia.objects.all()
    for x in lista_locais:
        dist = get_distances(local_busca, x.cidade, x.uf, lista_dist_atuais)
        if dist == 0:
            origem = f'{local_busca}'
            destino = f'{x.cidade}, {x.uf}'
            dist = gmaps_distances(origem, destino)
            new_distancia = Distancia(origem=local_busca, cidade_destino=x.cidade, uf_destino=x.uf, distancia=dist)
            new_distancia.save()  # salva no DB a nova distância calculada
            #  print(f'Origem: {local_busca:<20} Destino: {x.nomelocal:<20} - {x.cidade:<20} Distância: {dist} KM')
        lista_dist_calc[x.nomelocal] = dist
    lista_dist_sorted = sorted(lista_dist_calc.items(), key=itemgetter(1))
    return lista_dist_sorted
