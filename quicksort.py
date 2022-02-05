#Quicksort is a sorting algorithm. 
#Its much faster than selector sort and is frequently used in real life. 
#First it will take an array. 
# If the len(array) is less than 2
#It will return as it it. 
#Then if the len(Array) is more than 2
# It will take the first element as pivot. 
#Then there are two types of array : low[] & high[]
# low[] : will be array of numbers less than pivot
# high[] : will be array of numbers higher than pivot

#Algorithm to sort the aray.
def partition(array, low  , high):
    #Take the last array as pivot : 
    pivot = arr[high]
    #pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot :
            i =

#Quick Sort Algorithm
#It uses recursive method
def quickSort(arr , low, high ):
    #If the array size is less than 2 , it will be return as it is nm 
    if len(arr) < 2 :
        return arr
    else:
        pivot = arr[0]
        low = []
        high = []
        for num in arr : 
            if num < pivot : 
                #This will take array of numbers less than pivot
                low.append(num)
            else :
                #This will take array of numbers higher than pivot
                high.append(num)

arr = [3,10,6 , 9 , 1 , 2 , 5]
print('Initial Array : ' , arr)