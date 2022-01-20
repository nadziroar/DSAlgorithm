#Node class
from multiprocessing.dummy import current_process


class Node :
    #function to initialize the node object
    def __init__(self,  data):
        self.data = data #Assign Data
        self.next = None # Initialize text as NULL

#LinkedList class
class LinkedList :
    #function to initalize head
    def __init__(self):
        self.head = None

    #Function to insert a new node at the beggining
    def push(self , new_data):
        # 1 & 2 Allocate the node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new node
        self.head = new_node

    #Inserts a new node after the given prev_node, This defined inside LinkedList class shown above
    def insertAfter (self, prev_node, new_data):
        #1. Check if the given prev_node exists 
        if prev_node is None:
            print ('The given previous node must exist in LinkedList')
            return
        #2. Create new node
        #3. Put in the data
        new_node = Node(new_data)
        #4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        #5. Make next of prev_node as new_node
        prev_node.next = new_node

    #Appends a new node at the end. This method is defined inside LinkedList class shown above
    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
        # 4. If the LinkedList is empty, the make the new node as head
        if self.head is None:
            self.head = new_node
            return
        #5. Else traverse till the last node
        last = self.head
        while(last.next):
            last=last.next
        #6.Change the next of last node
        last.next = new_node

    #Given a reference to the head of a list and a key,
    #Delete the first occurence of key in linkedlist
    def deleteNode(self,key):
        #Store head node
        temp = self.head
        #If head node itself holds the key to be deleted
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        #Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        #If key was not present in LinkedList
        if(temp == None):
            return
        #Unlink the node from LinkedList
        prev.next = temp.next
        temp = None

    #Delete the node at a given position
    def deleteNodePosition (self, position):
        if self.head is None:
            return
        if position == 0 :
            self.head = self.head.next
            return self.head
        index = 0 
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position
                temp = current.next
                break
            prev = current 
            current = current.next
            index += 1
        prev.next = temp 
        return prev
     #This function prints content of linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



#Code Execution starts here
if __name__ == '__main__':
    #Start with empty list
    llist = LinkedList()

    #Insert 6 . So linkedlist becomes 
    # 6 -> None
    llist.append(6)

    #Insert 7 at the beggining. So LinkedList becomes
    # 7-> 6 -> None
    llist.push(7)

    #Insert 1 at the beginning. So LinkedList becomes 
    # 1 -> 7 -> 6 -> None
    llist.push(1)

    #Insert 8 , after 7. So Linkedlist becomes
    # 1 -> 7 -> 8 -> 6 -> 4 -> None
    llist.insertAfter(llist.head.next , 8)

    print ('Created Linked List is : ')

    llist.printList()

    llist.deleteNode(1)
    print('Linked List after Deletion of 1 : ')
    llist.printList()