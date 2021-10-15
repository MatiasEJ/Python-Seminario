import UTIL

def maximo(lista):
    i = 0
    mayor = lista[0]
    while i < len(lista):
        if (int(lista[i])>mayor):
            mayor=lista[i]
        i+=1
    return mayor

def menor(lista):
    i = 0
    menor = lista[0] 
    while i < len(lista):
        if (int(lista[i])<menor):
            menor=lista[i]
        i+=1
    return menor

def promedio(lista):
    total = 0
    for num in lista:
        total += num
    return total/len(lista) if len(lista)>0 else 0

def lineas_totales(archivo):
    fileref = open(archivo,'r')
    cant_lineas = len(fileref.readlines())
    fileref.close()
    return cant_lineas

def informe(archivo)-> list:
    fileref = open(archivo,'r')
    valores =[]
    for line in fileref:
        valores.append(int(line.split()[0]))
    fileref.close()

    return list((maximo(valores),menor(valores),promedio(valores),lineas_totales(archivo)))

def main():
    UTIL.clear_screen()
    resultados = informe("ej_7.txt")
    print(resultados)

main()