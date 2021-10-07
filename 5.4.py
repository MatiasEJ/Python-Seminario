def word_count(word:str)->int:
    n_words = 0
    for _ in word.split():
        n_words += 1
    return n_words

def longest_word(text):
    long_word = ""
    cadena = text.split()
    i = 0
    while i < (len(cadena)):
        if len(cadena[i]) > len(long_word):
            long_word = cadena[i]
        i +=1
    return long_word

def smallest_word(text):
    small_word = longest_word(text)
    cadena = text.split(" ")
    i = 0
    print(cadena)
    while i < (len(cadena)):
        if len(cadena[i]) < len(small_word) :
            small_word = cadena[i]
        i +=1
    return small_word

def main():
    text = input("Ingrese el texto: ")
    n_words = word_count(text)
    long_word = longest_word(text)
    small_word = smallest_word(text)
    print("El texto tiene {} palabras, la de mayor longitud es \"{}\" y la de menor longitud es \"{}\". ".format(n_words,long_word,small_word))

main()