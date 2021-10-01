#Figuras
def dibujarA(b,car,esp):
    col = 0
    for _ in range(0,b):
        for _ in range (0,b):
            col += 1
            print("{}".format(car),end= esp)
            if(col == b):
                print("\n")
                col = 0
                
def dibujarH(b,car,esp):
    print ("* "*b)
    for _ in range(b-2):
        print ("* "+ "  "*(b-2) + "* ")
    print ("* "*b)
                

def dibujarB(b, car,esp):
    print("\n")
    col = 0
    for n in range(0,b):
        for j in range (0,b):
            col += 1
            #Aca dijuja
            if((n == 0 or n == b-1) or (j==0 or j== b-1)  ):
                print("{}".format(car),end= esp)
            else:
                print(" ",end=" ")
            #----
        col = saltoLinea(col,b)

def dibujarC(b, car,esp):
    print("\n")
    col = 0
    cont = b
    for n in range(0,b): #filas
        
        for j in range (0,cont): #cols
            col += 1
            #Aca dijuja
            print("{}".format(car),end= esp)

        col = saltoLinea(col,cont)
        cont -= 1
        
def saltoLinea(col,b):        
    if(col == b): #SAlTO DE LINEA
        print("\n")
    return 0
           

   
        
    

def main():
#     dibujarA(4,"*"," ")
#     dibujarB(4,"*"," ")
    dibujarC(5,"*"," ")
#     dibujarH(4,"*"," ")
main()
