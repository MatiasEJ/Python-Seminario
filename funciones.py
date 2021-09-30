# 2.1
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
# 2.2
def producto(num1,num2):
    arr = list(str(num1))
    print("{:20d}".format(num2))
    print("x{:19d}".format(num1))
    print("-"*20)
    print("{:20d}".format(int(arr[2])*num2))
    print("+{:18d}-".format(int(arr[1])*num2))
    print("{:18d}--".format(int(arr[0])*num2))
    print("-"*20)
    print("{:20d}".format(num2*num1))
    

producto(456,123)
# 2.3

    def areaCirc(radio):
        return (math.pi) *(radio**2)

    def areaCuad(lado):
        return pow(lado,2)
        
    def areaNegra(lado,c1,c2):
        return areaCuad(lado)-areaCirc(c1/2)*2-areaCirc(c2/2)



# 2.4


def main():
    tot=areaCuad(12)
    porcen=(areaNegra(12,4,8)*100)/tot
    areane = areaNegra(12,4,8)
    print("------")
    print("El area negra es {:.2f} y es un {:.2f}%".format(areane,porcen))

main()