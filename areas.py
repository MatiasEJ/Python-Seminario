def areaCirc(radio):
    return 3.14*(radio**2)

def areaCuad(lado):
    return pow(lado,2)
    
def areaNegra(lado,c1,c2):
    return areaCuad(lado)-areaCirc(c1/2)*2-areaCirc(c2/2)

tot=areaCuad(12)
porcen=(areaNegra(12,4,8)*100)/tot
areane = areaNegra(12,4,8)
print("------")
print("{}".format(areaCuad(12)))
print("El area negra es {:.2f} y es un {:.2f}%".format(areane,porcen))
