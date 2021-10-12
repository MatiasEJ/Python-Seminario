import random
from ej_61 import estaEnLista

def cargarLista() -> list:
    print('Ingrese numeros enteros positivos, para finalizar ingrese 0: ')
    num = int(input(""))
    lista = []
    while num != 0:
        if num < 1: 
            print("Error,numero no positivo")
            num = int(input(""))
        elif estaEnLista(num,lista): 
            print("Error, numero ya esta en la lista")
            num = int(input(""))
        else:
            lista.append(num)
            num = int(input(""))
    return lista
    

def cargarLista2(lista: list) -> list:
    nuevaList = rem_dups(lista)
    nuevaList = rem_negativos(nuevaList)
    return nuevaList   

def rem_dups(lista: list) -> list:
    nuevaLista = []
    for num in lista:
        if num not in nuevaLista:
            nuevaLista.append(num)
    return nuevaLista

def rem_negativos(lista:list):
    nuevaLista = []
    for num in lista:
        if int(num) > 1 :
            nuevaLista.append(num)
    return nuevaLista


def main():
    # lista = cargarLista()
    # print(lista)
    lista = [-1,-2,5,0,1,1,1,3,3,4,5]
    # print(lista)
    lista2 = cargarLista()
    print(lista2)
    # lista = rem_dups(lista)
    # print(lista)
    # rem_negativos(lista)

main()
