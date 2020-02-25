import requests

uf = 35    # UF = São Paulo
request = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')
res = request.json()
for x in res:
    print(x)

request = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
res = request.json()
cont = 0
for x in res:
    cont += 1
    print(f'{cont} - {x["id"]} - {x["nome"]} - {x["sigla"]} - {x["regiao"]["nome"]}')
