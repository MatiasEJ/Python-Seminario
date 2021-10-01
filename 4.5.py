#ESPRIMO
def esPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
def imprimirPrimo(cant):
    col = 0
    for n in range (2,cant+1):
        if(esPrimo(n)):
            col += 1
            print("{:4}{:<4}".format(" ",n),end= " ")
            if(col == 10):
                print("\n")
                col = 0

def imprimirPrimos(cant):
    print("\n")
    col = 0
    total = 0
    n = 2
    while (total < cant):
        if(esPrimo(n)):
            total+=1
            col += 1
            print("{:4}{:<4}".format(" ",n),end= " ")
            if(col == 10):
                col = 0
                print("\n")
        n += 1


def main():
    cant = int(input("Ingrese cantidad (n natural): "))
    imprimirPrimo(cant)
    print("\n"*2)
    imprimirPrimos(cant)

            
             
main()