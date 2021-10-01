#5 cadenas

def principioFin(text):
    txt = text.split()
    primerP = deformatear(txt[0])
    ultimaP = deformatear(txt[-1])
    print(primerP)
    print(ultimaP)
    return primerP == ultimaP

def deformatear(palabra):
    pal = (palabra.split("!"))
    if("" in pal):
        pal.remove("")
    return toLowerCase(pal[0])
    
def toLowerCase(text):
    i = 0
    ch2 = ''
    while text[i:]:
        ch = ord(text[i])
        if ch > 64 and ch < 91:
            ch2 += chr(ch+32)
        else:
            ch2 += chr(ch)
        i += 1
    return ch2

def main():
    txt = "gaTo de poca fe, he dicho! Vamos, vamos GATO!"
    if(principioFin(txt)):
        print("El texto cumple la condición.")
    else:
        print("El texto no cumple la condición.")
        
    
main()
        