#This is file for stack DS 
#
#

#Stack by using List 
from inspect import stack


list_of_stacks = []
#append() function to push element in the stack
list_of_stacks.append('Item 1')
list_of_stacks.append('Item 2')
list_of_stacks.append('Item 3')

print('The Initial Stack')
print(list_of_stacks)

#Pop() function to pop elements
#LIFO Order
print('\n Element popped from Stack : ')
print (list_of_stacks.pop())
