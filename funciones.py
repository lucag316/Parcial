'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import json

def cargar_json(path:str):
    with open(path, "r") as file:
        file = json.load(file)
        return file["results"]


def buscar_minimo(lista_heroes:list, key:str):
    minimo = 0
    for i in range(len(lista_heroes)):
        if(lista_heroes[i][key] < lista_heroes[minimo][key]):
            minimo = i
            
    return minimo

    
def buscar_maximo(lista_heroes:list, key:str):

    maximo = 0
    for i in range(len(lista_heroes)):
        if(lista_heroes[i][key] > lista_heroes[maximo][key]):
            maximo = i

    return maximo

def ordenar_personajes_altura(lista_heroes:list, key:str):

    lista_a_ordenar = lista_heroes.copy()
    lista_ordenada = []

    while len(lista_a_ordenar) > 0:

        indice_minimo = buscar_minimo(lista_a_ordenar, key)
        elemento_minimo = lista_a_ordenar.pop(indice_minimo)
        lista_ordenada.append(elemento_minimo)
        
        
    return lista_ordenada
