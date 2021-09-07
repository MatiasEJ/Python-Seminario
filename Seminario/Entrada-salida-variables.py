#1.1
def primerEj():
    numero = input("Ingrese numero: ")
    print("Usted ingresó: {}".format(numero))

#1.2
def segundoEj():
    l1 = input("Ingrese Lado 1: ")
    l2 = input("Ingrese Lado 2: ")
    areaPerim(l1,l2)

def areaPerim (lado1, lado2):
    print("Perimetro :", int(lado1)*2+int(lado2)*2)
    print("Area :", int(lado1)*int(lado2))
   
def main():
#     primerEjercicio()
    segundoEj()
main()
