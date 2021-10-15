import UTIL

def informe(archivo)-> list:
    fileref = open(archivo,'r')
    valores =[]
    for line in fileref:
        vals = line.split()
        print(vals)
    fileref.close()
    return valores

def main():
    UTIL.clear_screen()
    nombre_arch= input("Archivo a abrir: ")
    archivo = informe(nombre_arch+".txt")
    print(archivo)


main()