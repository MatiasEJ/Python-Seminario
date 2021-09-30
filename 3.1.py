# 3.1
def operar(num1, num2, operacion):
    resultado = 0
    if(operacion == '/'):
        resultado = num1 / num2
    elif(operacion == '//'):
        resultado = num1 // num2
    elif(operacion == '+'):
        resultado = num1 + num2
    elif(operacion == '-'):
        resultado = num1 - num2
    elif(operacion == '*'):
        resultado = num1 * num2
    elif(operacion == '**'):
        resultado = num1 ** num2
    return resultado
        
def main():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese el segundo numero: ")
    print("{} {} {} = {}".format(num1,operacion,num2,operar(num1,num2,operacion)))
    
main()