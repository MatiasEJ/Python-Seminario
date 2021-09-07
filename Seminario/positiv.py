def positividad(num):
    res = ""
    if(num == 0):
        res = "cero"
    elif(num < 0):
        res = "negativo"
    elif(num > 0):
        res = "positivo"
    return res

def tipoNum(num):
    res = ""
    if(num%1 != 0):
        res = "real"
    else:
        res = "entero"
#     elif(num == 0 and num/num == 1):
#         res = "entero"
    if(num>=1 ):
         res = res + " natural"    
    
    
    
    return res
    

def main():
    num = float(input("meteme un numerito roberto: "))
    pos = positividad(num)
    tipo = tipoNum(num)
    print("El numero es {} y {}".format(pos,tipo))
    
main()