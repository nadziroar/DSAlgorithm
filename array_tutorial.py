"""This is tutorial about Array: """

#Python Array 

#Array example of food ordering
from array import array
from itertools import count
from xxlimited import foo


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



