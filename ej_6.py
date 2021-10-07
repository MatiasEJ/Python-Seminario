import random

def estaEnLista(num:int,lst:list)-> bool:
    return num in lst

def estaEnLista2(num:int,lst:list)-> bool:
    res = False
    for n in lst:
        if n == num:
            res = True
    return res 

def estaEnLista3(num: int,lst: list)-> bool:
    i=0
    res = False
    while i < len(lst):
        if num == lst[i]:
            res = True
        i +=1
    return res

def listaRandom(ini,fin):
    lista = []
    for _ in range(ini,fin):
        lista.append(random.randint(ini,fin))
    return lista

def main():
    lista= listaRandom(-2,2)
    num = 10
    print(lista)
    print(estaEnLista(num,lista))
    print(estaEnLista3(0,lista))

main()
