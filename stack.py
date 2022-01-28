#This is file for stack DS 
#1. 
# Implementation using List
#2. Implementation using Dequeue
#3. Implementation using

#Stack by using List .
#However the list has a few shortcomings. As the list grows, the speed will be an issue.
# The items in the list are stored next to each other in memory, 
# if the stack grows bigger than the block of memory that currently holds it, 
# the Python needs to do some memory allocation.
from collections import deque
from queue import LifoQueue

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
# Deque is preferred over the list in the cases where we need quicker append and pop operations 
# from both the ends of the container, as deque provides an O(1) time complexity for append 
# and pop operations as compared to list which provides O(n) time complexity
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

print('Stack after elements are popped : ' ,deque_stacks)

#Implementation of stack using queue module
queue_stack = LifoQueue(maxsize= 3)
#To show the size of stack
print(queue_stack.qsize())
#Put() function to push element in the stack
queue_stack.put('Queue 1')
queue_stack.put('Queue 2')
queue_stack.put('Queue 3')

print('Full ' , queue_stack.full())
print('The size : ', queue_stack.qsize())


#Get() function to pop element from stack in
#LIFO order
print('Elements that get popped from the stack')
print(queue_stack.get())
print(queue_stack.get())
print(queue_stack.get())

print("Is the stack empty ? : " , queue_stack.empty())