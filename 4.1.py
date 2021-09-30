def tabla(num):
    for n in range(1,11):
        res = n * num
        print("{} x {:2} = {}".format(num,n,res))
        
def main():
    num = int(input("Ingrese Numero: "))
    tabla(num)

main()