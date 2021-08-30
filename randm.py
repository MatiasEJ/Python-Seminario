import random
def aleatorio(limInf, limSup):
    numGenerado = random.randint(limInf,limSup)
    return numGenerado
    

def main():
    
    limInf = int(input("Ingrese el limite inferior: "))
    limSup = int(input("Ingrese el limite superior: "))
    
    primerAleatorio = aleatorio(limInf,limSup)
    print( "1-Limite inferior {}, limite superior {}. Numero generado: \033[1;31;40m {}\033[0;0m".format(limInf,limSup,primerAleatorio))
    segundoAleatorio = aleatorio(limInf,limSup)
    print( "2-Limite inferior \033[1;31;40m {} \033[0;0m, limite superior {}. Numero generado: \033[1;34;40m {}\033[0;0m".format(primerAleatorio,limSup,segundoAleatorio))
    tercerAleatorio = aleatorio(limInf,limSup)
    print( "3-Limite inferior \033[1;31;40m {} \033[0;0m, limite superior \033[1;34;40m {}\033[0;0m Numero generado: {}".format(primerAleatorio,segundoAleatorio,tercerAleatorio))
    
main()