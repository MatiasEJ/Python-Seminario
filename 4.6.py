#Capicua
def esCapicua(num):
    #82428
    nu = ""
    un = ""
    for n in range(0,len(num)):
        nu += num[n]
    for n in range(len(num)-1,-1,-1):
        un += num[n]
        
    return nu == un

def main():
    print(esCapicua("8234328"))
    
main()