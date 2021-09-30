import random

def validar(inf,sup,num):
    return num in range(inf,sup+1)
        
def validarMsg(val):
    while(not validar(0,100,val)):
        val = int(input("Error, ingrese valor [1-99]: "))
    return val
        
def validarPar(par):
    while(not validar(-1,3,par)):
        par = int(input("Error, ingrese valor [0-2]: "))
    return par

def nombreFiltro(num):
    nombre = ""
    if (num == 0):
        nombre = "par"
    elif (num == 1):
        nombre = "impar"
    else:
        nombre = "ambos"
    return nombre

def filtrar(inf,sup,salto,filtro):
    inicio = inf
    print("{}".format(inicio))
    while(inicio < sup):
        
        if(filtro == 2):
            print("{}".format(inf*salto))
        elif(filtro == 1):
            if(inicio %3 ==0):
                print("{}".format(inf*salto))
        else:
            if(inicio %2 ==0):
                print("{}".format(inf*salto))
              
        inicio += salto
   
def main():
    inf = int(input("Ingrese limite inferior: "))
    inf = validarMsg(inf)
    
    sup = int(input("Ingrese limite superior: "))
    sup = validarMsg(sup)
   
    salto = int(input("Ingrese salto: "))
    salto = validarMsg(salto)
    
    filtro = int(input("Ingrese 0 par, 1 Impar, 2 ambos: "))
    filtro = nombreFiltro( validarPar(filtro))
    
    
            
    print("La secuencia entre {0} y {1}, de {2} en {2} y {3}:".format(inf,sup,salto,filtro ))
    filtrar(inf,sup,salto,filtro)
    
    
main()
