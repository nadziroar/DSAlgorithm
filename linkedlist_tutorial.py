#Node class
class Node :
    #function to initialize the node object
    def __init__(self,  data):
        self.data = data
        self.next = None

#LinkedList class
class LinkedList :
    #function to initalize head
    def __init__(self):
        self.head = None

    #This function prints content of linked list
    #Starting from head
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    #Function to insert a new node at the beggining
    def push(self , new_data):
        # 1 & 2 Allocate the node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node = self.head
        # 4. Move the head to point to new node
        self.head = new_node


#Code Execution starts here
if __name__ == '__main__':
    #Start with empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next  = third

    llist.printList()