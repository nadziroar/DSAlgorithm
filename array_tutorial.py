"""This is tutorial about Array: """

#Python Array 

#Array example of food ordering
from array import array
from itertools import count
from xxlimited import foo
    
#Function to find the partition position   
def partition (array , low, high) : 
    #choose the last in the array as pivot.
    pivot = array[high]
    #pointer for greater element
    i = low - 1
    #traverse through all elements
    #compare each element with pivot
    for j in range (low, high):
        if array[j] <= pivot:
            #if element smaller than pivot is found. swap it with the greater element pointed by i
            i = i + 1
            #swapping element at i with element at j
            (array[i] , array[j]) = (array[j] , array[i])
        #swapping element at i with element at j
        (array[i], array[j]) = (array[j], array[i])
    
    #swap the pivot element with the greater elementm specified by i
    (array[ i + 1],  array[high]) = (array[high] , array[i + 1])
    #return the position from where partition is done
    return i + 1

#Function to perform quicksort 
def quickSort (array , low, high):
    if low < high:
        #find pivot element such that 
        #element smaller than pivot are on the left
        #element greater than pivot are on the right
        
        pi = partition(array , low , high)
        #recursive call on the left of pivot
        quickSort(array , low , pi - 1)
        
        #recursive call on the right of pivot
        quickSort (array , pi + 1 , high)
    
    
array_num = [5, 10 , 9,3,1,7,19 , 15 , 16 , 12 , 8]
print ('unsorted array : ' , array_num)

size = len(array_num)
array_num = quickSort(array_num , 0 , size - 1)

print('Sorted Array in Ascending Order  : ',  array_num)


food_ordering = ['nasi lemak' , 'chicken chop' , 'ayam goreng' , 'roti canai' , 'lagsana']
food_ordering2 = ['kimchi' , 'sushi' , 'korean fried chicken']
#To view all array
print("All Food : " , food_ordering)
#To view item on specific index
print("Food on index 3 : " , food_ordering[3])
#Append = 
food_ordering.append('Healthy Breakfast Smoothie')
print ("After append(Healthy Breakfast Smoothie) : " , food_ordering)
#Pop = 
food_ordering.pop()
print("After  pop() : ", food_ordering)
#Clear =
food_ordering.clear()
print("After clear() : ", food_ordering)
#Copy = 
food_ordering = food_ordering2.copy()
print("After food_ordering2.copy() : " , food_ordering)
#Len= 
print("After len() : ", len(food_ordering))
#insert = 
food_ordering.insert(4, 'Roti Canai')
print("After insert : ", food_ordering)
#reverse = 
food_ordering.reverse()
print("After reverse : " , food_ordering)



