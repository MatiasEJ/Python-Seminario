def secuencia(inf,sup,salto):
    print("La secuencia entre {0} y {1}, de {2} en {2}".format(inf,sup,salto))
    for n in range(inf,sup+1,salto):
        print("{}".format(n))
        
def sec(inf,sup,salto):
    print("La secuencia entre {0} y {1}, de {2} en {2}".format(inf,sup,salto))
    inicio = inf
    print("{}".format(inicio))
    while(inicio <= (sup - salto)):
        print("{}".format(inicio+salto))
        inicio += salto
    

def main():
    inf = int(input("Ingrese limite inferior: "))
    sup = int(input("Ingrese limite superior: "))
    salto = int(input("Ingrese salto: "))
    sec(inf, sup, salto)
    
main()
