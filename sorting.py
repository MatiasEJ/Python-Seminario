import timeit
# SORTS
arr = [22,3,54,2,5,12,65,77,3]
# Bubble
def bubbleSortMin(array):
    length = len(array)
    for i in range(0,length):
        for j in range(0,length-1):
            if(array[j] > array[j+1]):
               swap(array,j)

def swap(arr,j):
    aux = arr[j+1]
    arr[j+1]= arr[j]
    arr[j] = aux

def bubbleSortMax(array):
    length = len(array)
    for i in range(0,length):
        for j in range(0,length-1):
            if(array[j] < array[j+1]):
                swap(array,j)
   
bubbleSortMax(arr)
print(arr)

# Insertion


