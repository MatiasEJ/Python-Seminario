#3.4

def iguales(num1,num2,num3):
    return num1 == num2 == num3

def distancias(num1,num2,num3):
    distancia = None
    max = None
    
    if(iguales(num1,num2,num3)):
        distancia = 0
    
    return distancia

print(iguales(1,1,1))
print("Distancia: ",distancias(1,2,3))