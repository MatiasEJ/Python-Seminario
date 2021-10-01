def esCapicua(num):
    nu = ""
    un = ""
    for n in range(0,len(num)):
        nu += num[n]
    for n in range(len(num)-1,-1,-1):
        un += num[n]
        
    return nu == un

def invertir(palabra):
    un = ""
    for n in range(len(palabra)-1,-1,-1):
        un += palabra[n]
    return un

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

def juntaPalabra(text):
    text = text.split()
    conv = ""
    for palabra in text:
        conv = conv + palabra
    return conv

def esPalindromo(text):
    text = toLowerCase(juntaPalabra(text))
    invertido = toLowerCase(invertir(juntaPalabra(text)))
    return text == invertido
    
def main():
    texto = "No deseo ese don "
    if esPalindromo(texto):
        print("la frase es palindroma!")
    else:
        print("la frase no es palindroma!")
    
main()