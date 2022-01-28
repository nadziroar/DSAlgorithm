#This is file for stack DS 
#
#


#Stack by using List .
#However the list has a few shortcomings. As the list grows, the speed will be an issue.
# The items in the list are stored next to each other in memory, 
# if the stack grows bigger than the block of memory that currently holds it, 
# the Python needs to do some memory allocation.
list_of_stacks = []
#append() function to push() element in the stack
list_of_stacks.append('Item 1')
list_of_stacks.append('Item 2')
list_of_stacks.append('Item 3')

print('The Initial List Stack')
print(list_of_stacks)

#Pop() function to pop elements
#LIFO Order
#It will pop from the leftmost list, which is the lastest element that was inserted
print('\n Element popped from List Stack : ')
print ('Pop() 1 : ' , list_of_stacks.pop())
print ('Pop() 2 : ' , list_of_stacks.pop())
print ('Pop() 3 : ' , list_of_stacks.pop())

print('Stack after being popped() : ' , list_of_stacks)

#Implementations using collections.deque: 
deque_stacks = deque()

#Append() function to push() element in the stack
deque_stacks.append('Deque 1')
deque_stacks.append('Deque 2')
deque_stacks.append('Deque 3')

print('Initial Deque Stack : ' , deque_stacks)

#Pop() function to pop the element from stack 
#LIFO order 
print('Element popped from stack : ')
print(deque_stacks.pop())
print(deque_stacks.pop())
print(deque_stacks.pop())

print('Stack after elements are popped : ' , deque_stacks)
print 