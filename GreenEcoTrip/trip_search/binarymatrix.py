import numpy as np
from itertools import product
import time

def get_number_of_places(datas):
    return len(set(([i['Inbounds']['Name'] for i in datas]) + ([i['Inbounds']['Name2'] for i in datas])))


def get_list_of_places(datas):
    return set(([i['Inbounds']['Name'] for i in datas]) + ([i['Inbounds']['Name2'] for i in datas]))


def get_travel_tuples(datas):
    return zip(([i['Inbounds']['Name'] for i in datas]), ([i['Inbounds']['Name2'] for i in datas]))


def create_adjacency_matrix(places, edges):
    matrix = product(places, places)
    matrix = [(i, j, 1) if ((i, j) in edges or (j, i) in edges) else (i, j, 0) for (i, j) in matrix]
    return matrix


def maronna(Partenza, Arrivo, Durata):
    dati2 = {}
    dati2['Inbounds'] = {}
    dati2['Outbounds'] = {}
    dati2['Something'] = {}
    dati2['Inbounds']['Name'] = Partenza
    dati2['Inbounds']['Name2'] = Arrivo
    dati2['Inbounds']['Duration'] = Durata
    return dati2


if __name__ == '__main__':
    dati1 = maronna('Parigi', 'Berlino', 1234)
    dati2 = maronna('Parigi', 'Svezia', 54321)
    dati3 = maronna('Venezia', 'Londra', 222)
    dati4 = maronna('Barcellona', 'Venezia', 2)

    veridati = [dati1, dati2, dati3, dati4]

    print("LIST RESULT", veridati)
    print('len', get_number_of_places(veridati))
    names = get_list_of_places(veridati)
    print('nomi', names)
    couples = list(get_travel_tuples(veridati))
    print('corse', couples, '\n')

    t = time.time()
    matrix = create_adjacency_matrix(names, couples)
    print(time.time() - t)
    print(np.linspace(0, 36, 7)[:-1])

    for i in np.linspace(0, 36, 7)[:-1]:
        print(matrix[int(i):int(i + 6)])
