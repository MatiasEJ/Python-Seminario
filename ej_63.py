from UTIL import *
from ej_61 import estaEnLista

def menu():
    print("1. CARGAR CONJUNTOS")
    print("2. UNION")
    print("3. INTERSECCION")
    print("4. DIFERENCIA (A-B)")
    print("5. DIFERENCIA SIMETRICA")
    print("6. SALIR")

def operaciones(num)-> int:
    while num != 6:
        if(num == 1):
            print("1. CARGAR CONJUNTOS")
            num = 6
        elif(num == 2):
            print("2. UNION")
        elif(num == 3):
            print("3. INTERSECCION")
        elif(num == 4):
            print("4. DIFERENCIA (A-B)")
        elif(num == 5):
            print("5. DIFERENCIA SIMETRICA")
        elif(num == 6):
            print("6. SALIR")
            num = 6
        menu()
        num = int(input("Elija una opcion del menu: "))
def mayorTupla(a):
    return a[0] if len(a[0])>len(a[1]) else a[1]
def menorTupla(a):
    return a[0] if len(a[0])<len(a[1]) else a[1]

def cantVeces(num, lista):
    cant = 0
    for n in lista:
        if n == num:
            cant += 1
    return cant

def union(conjA,conjB):
    return list(rem_dups(conjA+conjB))

def interseccion(a: tuple):
    lista = []
    i = 0
    while i < len(mayorTupla(a)):
        for num in mayorTupla(a):
            if num in menorTupla(a):
                lista.append(num)
        i+=1
    return rem_dups(lista)

def diferenciaAB(a:tuple):
    lista = a[0]
    i = 0
    while i < len(a[0]):
        for num in a[1]: 
            if num in a[0]: 
                lista.remove(num)
        i+=1
    print("diferencia AB",lista)


def cargar_conjuntos(listaA,listaB):
    print("CARGA conjunto A")
    listaA = cargarLista(listaA)
    print(listaA)
    print("CARGA conjunto B")
    listaB = cargarLista(listaB)
    print(listaB)

def cargarLista(lista:list) -> list:
    print('Ingrese numeros enteros positivos, para finalizar ingrese 0: ')
    num = int(input(""))
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
    
def diferenciaSimetrica(a:tuple):
    un = union(a)
    inter = interseccion(a)
    i = 0
    nuevo = []
    while i < len(un):
        if un[i] not in inter:
            nuevo.append(un[i])
        i += 1
    print("diferencia sim", nuevo)


def main():
    # menu()
    # num = int(input("Elija una opcion del menu: "))
    # operaciones(num)
    # print("-------fin-------")
    clear_screen()
    conjA = []
    conjB = []
    tupl = (conjA,conjB)
    cargar_conjuntos(conjA,conjB)
    print("union", union(conjA,conjB))
    print ("inter ",interseccion(tupl))
    diferenciaAB(tupl)
    diferenciaSimetrica(tupl)


main()