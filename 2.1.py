def imprimir(dias,horas,minutos,segundos):
    print("Dias({:f}), horas({:f}), minutos({:f}),segundos({})".format(dias,horas,minutos,int(segundos)))

def convertir(tiempo):
    print("convirtiendou...")
    
    dias=tiempo/(86400)
    horas= (dias%1) * 24 
    
    minutos=(horas%1)*60
    segundos=(minutos%1)*60
    imprimir(dias,horas,minutos,segundos)


def main():
     num1 = int(input("Ingrese tiempo en segundos: "))
     convertir(num1)
main()