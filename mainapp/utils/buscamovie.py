import requests

request = requests.get(f'http://127.0.0.1:8000/movies/')

resultado = request.json()

print(resultado[0])
print(resultado[0]['nome'])
print(resultado[0]['receita'])
print(resultado[0]['genero'])

print(resultado[1])
print(resultado[1]['nome'])
print(resultado[1]['receita'])
print(resultado[1]['genero'])

ano = 2020
request = requests.get(f'http://127.0.0.1:8000/yearmovies/{ano}')

resultado = request.json()

print(resultado[0])
print(resultado[0]['nome'])
print(resultado[0]['receita'])
print(resultado[0]['genero'])

print(resultado[1])
print(resultado[1]['nome'])
print(resultado[1]['receita'])
print(resultado[1]['genero'])

request = requests.get(f'http://127.0.0.1:8000/topmovies/0')

resultado = request.json()

print(resultado[0])
print(resultado[0]['nome'])
print(resultado[0]['receita'])
print(resultado[0]['genero'])

print(resultado[1])
print(resultado[1]['nome'])
print(resultado[1]['receita'])
print(resultado[1]['genero'])

nome = 'titanic'
request = requests.get(f'http://127.0.0.1:8000/searchmovies/{nome}')

resultado = request.json()

print(resultado[0])
print(resultado[0]['nome'])
print(resultado[0]['receita'])
print(resultado[0]['genero'])

print(resultado[1])
print(resultado[1]['nome'])
print(resultado[1]['receita'])
print(resultado[1]['genero'])
