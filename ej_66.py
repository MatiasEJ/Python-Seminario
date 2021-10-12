import os

def agregarDicEle(dic: dict):
    print(dic)
    idiomas = ["en","sp","de"]
    msg = "Ingresar un numero a traducir o cero para salir: "
    key = int(input(msg))
    print(key)
    while key != 0 and key != "" and key != "\n":
        agregar_traducciones(idiomas,key, dic)

        key = toma_key(msg)
    print("\n",dic)

def agregar_traducciones(idiomas:list,key,dic:dict):
    cant_idiomas = len(idiomas)
    traducciones = []
    index = 0
    for i in idiomas:
        if(index < cant_idiomas):
            traducciones.append(input(f"{i}: "))
            index += 1
    dic.update({key:tuple(traducciones)})

def toma_key(msg):
    key = int(input(msg))
    if(key == 0):
        print("\n\n-----fin-del-programa----")
    return key

# def agregarDicEle(dic: dict,idiomas: tuple):
#     key = int(input("ingresar un numero a traducir o cero para salir: "))
#     while key != 0 and key != "":
#         traducciones = agregar_traducciones(idiomas, dic)
        
#         dic.update({key:tuple(traducciones)})

#         key = int(input("ingresar un numero a traducir o cero para salir: "))
#         if(key == 0):
#             print("-----fin----")



def traductor(dic):
    print(dic)
    idiomas = ("en","sp","de")
    msg = "ingresar un numero a traducir o cero para salir: "
    error = "ERROR: "
    key = int(input(msg))
    print("la key: {}".format(key) )
    while key != 0 and key != "" :
        if(key not in dic.keys()):
            key = input(error + msg)
        else:
            valores = dic.get(key) #Obtiene la tupla de traduccion
            traduccion= search_lang(valores,idiomas)
            print("{} en {}: {}".format(key,traduccion[1],traduccion[0]))
            key = toma_key(msg) 
    print("\n",dic)

def search_lang(key:tuple,idiomas)-> tuple:
    """Devuelve una tupla de (traduccion, idioma)"""
    error = "ERROR: " 
    msg_idioma ="Ingresar idioma [{}]: ".format(impr_lista_idiomas(idiomas)) 
    lang = input(msg_idioma)
    while lang != 0 :
        if (lang in idiomas):
            if lang == 'en':
                valor=(key[0],"Ingles")
            elif lang == 'sp':
                valor=(key[1],"Español")
            elif lang == 'de':
                valor=(key[2],"Aleman")
            lang = 0 
        else:
            lang = input(error+msg_idioma)
    return valor

def impr_lista_idiomas(idiomas):
    concatIdiomas = ""
    for i in idiomas:
        concatIdiomas += f" '{i}'| "
    return concatIdiomas

def clear_screen():
    print("\n")
    os.system('cls')

def main():
    # idiomas = [(0,"en","Ingles"),(1,"sp","Español"),(2,"de","Aleman")]
    clear_screen()
    diccionario={       
        1:("one","uno","gnochi"),
        3:("three","tres","triochi"),
        4:("four","cuatro","cuatrochi")
    }
    
    # agregarDicEle(diccionario)
    traductor(diccionario)

main()