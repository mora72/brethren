import requests

cliente = '1'

request = requests.get(f'http://127.0.0.1:8000/clientes/{cliente}/')

resultado = request.json()

print(resultado)
print(resultado['nome'])
print(resultado['endereco'])
print(resultado['idade'])
