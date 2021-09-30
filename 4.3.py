#PARIDAD

def nombreParidad(val):
    nombre = ""
    if val == 2:
        nombre = "ambos"
    elif val == 1:
        nombre = "impar"
    else:
        nombre = "par"
    return nombre

def imprimeParidad(paridad, num):
    if(paridad == 2):
        print("{}".format(num))
    elif(paridad == 1 and num%3 == 0):
        print("{}".format(num))
    elif(paridad == 0 and num%2 == 0):
        print("{}".format(num))

def sec(inf,sup,salto,paridad):
    inicio = inf
    print("{}".format(inicio))
    while(inicio <= (sup - salto)):
        num = inicio + salto
        imprimeParidad(paridad,num)

        inicio += salto
    

def main():
    inf = int(input("Ingrese limite inferior: "))
    sup = int(input("Ingrese limite superior: "))
    salto = int(input("Ingrese salto: "))
    paridad = int(input("Ingrese paridad -> \"0(par), 1(impar),2(ambos)\": "))
    print("La secuencia entre {0} y {1}, de {2} en {2} y {3}".format(inf,sup,salto,nombreParidad(paridad)))
    sec(inf, sup, salto,paridad)
    
main()
