#3.5
def bono(sueldo):
    return (0.15*sueldo) if sueldo > 2000 else (0.2*sueldo)

def plusC(sueldoBase,categoria):
    plusc = None
    if( categoria >= 1 and categoria <=3 ):
        plusc = 0.1
    elif(categoria >= 4 and categoria <= 6):
        plusc = 0.12
    elif(categoria >= 7 and categoria <=9):
        plusc = 0.2
    else:
        plusc = 0
    return plusc*sueldoBase

def plusH(sueldoBase, hijos):
    return (0.05*sueldoBase) if hijos else 0

def plus(sueldo,hijos,categoria):
    plusCategoria = None
    if(hijos == True and categoria <= 6):
        plusCategoria = plusC(sueldo,categoria) + plusH(sueldo,hijos)
    else:
        plusCategoria = plusC(sueldo,categoria) 
    return plusCategoria

    

def main():
    sueldoBase = int(input("Ingrese el sueldo base: "))
    hijos = bool(True if input("Tiene hijos(s/n): ") == "s" else False )
    categoria = int(input("Ingrese categoria: "))
    print(hijos)
    print("BONO ",bono(sueldoBase))
    print("H ",plusH(sueldoBase,hijos))
    print("C ",plusC(sueldoBase,categoria))
    print("PLUS ",plus(sueldoBase,hijos,categoria))
    print("El sueldo total sera de: " ,sueldoBase+bono(sueldoBase)+plus(sueldoBase,hijos,categoria))
    
    
main()


