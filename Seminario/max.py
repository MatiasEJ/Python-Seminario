# def max2(a,b):
#     max = None
#     if(a>b):
#         max = a
#     else:
#         max = b
#     return max

def max2(a,b):
    return a if a > b else b
def minDosArgs(a,b):
    return a if a < b else b

def minTresArgs(a,b,c):
    min = None
    if(minDosArgs(a,b) == a == minDosArgs(a,c) ):
      min = a
    elif(minDosArgs(a,b) == b == minDosArgs(b,c)):
      min = b
    else:
        min = c
    return min

def maxTresArgs(a,b,c):
    max = None
    if(max2(a,b) == a == max2(a,c) ):
       max = a
    elif(max2(a,b) == b == max2(b,c)):
       max = b
    else:
       max = c
    return max

def medio(a,b,c):
    max = maxTresArgs(a,b,c)
    min = minTresArgs(a,b,c)
    inter = None
    if(max != a != min):
        inter = a
    elif(max  != b != min):
        inter = b
    else:
        inter = c
    return inter
    
    
def isEqualDist(a,b,c):
    max = maxTresArgs(a,b,c)
    min = minTresArgs(a,b,c)
    med = medio(a,b,c)
    promedio = (max + min) / 2
    msg="Estan igualmente distanciados!"
    return msg if promedio == med else ("No "+ msg)  
    
    

    


def main():
    msg = "Ingrese el primer numero: "
    a = int(input(msg))
    b = int(input("Ingrese el primer numero: "))
    c = int(input("Ingrese el primer numero: "))
    print(isEqualDist(a,b,c))
    
    
main()