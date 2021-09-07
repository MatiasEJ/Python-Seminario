#Reverse String
def reverse(str):
    return str[::-1]
#merge Arrays
def merge(arr1, arr2):
    newArr = []
    first1 = arr1[0]
    first2 = arr2[0]
    i = 1
    j = 1
    while(first1 or first2 or not first1):
        if(first1 < first2):
            newArr.push(first1)
            first1 = arr1[i]
        else:
            newArr.push(first2)
            first2 = arr2[i]
            
    return newArr
    
    
def main():
    a = input("Ingrese palabra: ")
    print("reverse: ", reverse(a))
    print("merge: ", merge([3,4,1],[2,5,6]))
    

main()