def word_count(largo:str,corto:str)->int:
    n_palabras = 0
    for palabra in largo.split():
        if corto == palabra:
            n_palabras += 1
    return n_palabras

def main():
    largo = input("Ingrese el texto largo: ")
    corto = input("Ingrese el texto corto: ")    
    n_palabras = word_count(largo,corto)
    print(f"El texto corto se encontro {n_palabras} veces en el texto largo.")

main()