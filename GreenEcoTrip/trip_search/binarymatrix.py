import numpy as np


def get_number_of_places(datas):
    return len(set(([i['Inbounds']['Name'] for i in datas]) + ([i['Inbounds']['Name2'] for i in datas])))

def get_list_of_places(datas):
    return set(([i['Inbounds']['Name'] for i in datas]) + ([i['Inbounds']['Name2'] for i in datas]))

def get_travel_tuples(datas):

    return zip(([i['Inbounds']['Name'] for i in datas]),([i['Inbounds']['Name2'] for i in datas]))




def createbinarymatrix(names, couples):
    n = len(names)
    matrix = np.zeros((n,n))
    matrix = np.asmatrix(matrix)

    for i in matrix:
        for j in matrix:
            if (i,j) == couples[i]:
                matrix[i,j] = 1

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
    names= get_list_of_places(veridati)
    print( 'nomi',  names)
    couples= list(get_travel_tuples(veridati))
    print('corse',couples)
    print('matrix', createbinarymatrix(names,couples))
