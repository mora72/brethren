from ..models import Local
from operator import itemgetter
from ..distcalcmodule import *


def calcula_distancia(local_busca, uf_busca):
    lista_locais = Local.objects.all().order_by('criado')
    #  print(f'local busca dentro: {local_busca}')
    #  print(f'UF busca dentro: {uf_busca}')
    lista_distancias = {}
    for x in lista_locais:
        if uf_busca == x.uf:
            origem = f'{local_busca}'
            destino = f'{x.cidade}, {uf_busca}'
            dist = gmaps_distances(origem, destino)
            lista_distancias[x.nomelocal] = dist
            #  print(f'Origem: {local_busca:<20} Destino: {x.nomelocal:<20} - {x.cidade:<20} Distância: {dist} KM')
    lista_dist_sorted = sorted(lista_distancias.items(), key=itemgetter(1))
    return lista_dist_sorted
