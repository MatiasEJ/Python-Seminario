# 3.3
def isFechaValida(dia,mes,año):
    return checkDia(dia) and checkMes(mes) and checkCantDias(dia,año)
    
def checkCantDias(dia,año):
    return dia<=29 and isAñoBisiesto(año)     

def checkDia(dia):
    return dia >= 1 and dia<=31
            
def checkMes(mes):
    return mes >= 1 and mes <= 12

def isAñoBisiesto(año):
    return (año%4==0 and (año%100 !=0 or año%400==0))
   
# MEPA QUE la fecha 5/12/1903 aparece como correcta pero no lo es

def main():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    rta = "correcta" if (isFechaValida(dia,mes,año) == True) else "incorrecta"
    print("La fecha es {}".format(rta))

main()