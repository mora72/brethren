#  import googlemaps
import pickle

#  gmaps = googlemaps.Client(key='AIzaSyAimWq9887tTblf_rtp5nCDnTk4-TB74Hg')

#  geocode_result = gmaps.geocode("Barueri")
#  print(geocode_result)

file = open('/Users/carlo/PycharmProjects/brethren/arquivos/base.pck1', 'rb')
lista = pickle.load(file)
directions = lista[0]
distance = lista[1]
file.close()
print(directions[0]['legs'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])

#  directions = gmaps.directions('Uberlandia', 'São Paulo')
#  distance = gmaps.distance_matrix('Uberlandia', 'São Paulo')

#  file = open('/Users/carlo/PycharmProjects/brethren/arquivos/base.pck1', 'wb')
#  pickle.dump([directions, distance], file)
#  file.close()
