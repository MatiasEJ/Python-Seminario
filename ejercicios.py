num:float = 32.043
numero2:int = int(num//1)
print("entera "+ str(numero2) )
print("decimal "+str(num%1))

def imprimir(dias,horas,minutos,segundos):
    print("Dias({:.0f}), horas({:.0f}), minutos({:.0f}),segundos({})".format(dias//1,horas//1,minutos//1,int(segundos)))

def convertir(tiempo):
    print("convirtiendou...")
    
    dias=tiempo/(86400)
    horas= (dias%1) * 24 
    
    minutos=(horas%1)*60
    segundos=(minutos%1)*60
    imprimir(dias,horas,minutos,segundos)


convertir(93714)