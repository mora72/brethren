import requests

cep = '06472001'

request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

res = request.json()

print(res)
print(res['bairro'])
print(res['localidade'])
