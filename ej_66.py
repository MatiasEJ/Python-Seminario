def agregarDicEle(dic: dict):
    cantElementosTupla = 3
    key = int(input("ingresar un numero a traducir o cero para salir: "))
    val:list=[]
    while key != 0 and key != "":
        for _ in range(0,cantElementosTupla):
            val.append(input(" "))
        if val == "":
            key = input(f"ERROR: ingresar numero a traducir o cero apra salir: ")
            val = input(f"{key} -> ")
        
        dic.update({key:tuple(val)})
        val:list=[]
        key = int(input("ingresar un numero a traducir o cero para salir: "))
        if(key == 0):
            print("-----fin----")

def traductor(num,lang,dic:dict):
    llave = 0
    for key in dic.keys():
        print(key)
        if key == num:
            llave = key
        else:
            llave = 0
    for val in dic.values():
        print(val)
        lista = list(val)
        for i in len(lista):
            if lan == lang:
                print(lista)



def main():
    disio = {}
    disionario = {
        1:("uno","one","gnochi"),
        3:("tres","three","triochi"),
        4:("cuatro","four","cuatrochi")
    }
    # agregarDicEle(disio)
    print(disionario)
    traductor(3,'en',disionario)


main()