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
    
def main():
    num1 = int(input("Ingrese el multiplicando: "))
    num2 = int(input("Ingrese el multiplicador: "))
    producto(num2,num1)    
main()

