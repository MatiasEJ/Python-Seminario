def agregarDicEle(dic: dict):
    key = int(input("ingresar un numero a traducir o cero para salir: "))
    while key != 0:
        val = input("{} -> ".format(key))
        if val == "":
            key = input(f"ERROR: ingresar numero a traducir o cero apra salir: ")
            val = input(f"{key} -> ")
        dic.update({key:val})
        print(dic)
        key = int(input("ingresar un numero a traducir o cero para salir: "))
        if(key == 0):
            print("-----fin----")

def main():
    disio = {}
    print(disio)
    agregarDicEle(disio)
    print(disio)

main()