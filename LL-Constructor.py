class Node:
    def __init__(self, value):#create new node.
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)#calls the node class and pass the value to node class.
        self.head = new_node#to make head pointer points to new node.
        self.tail = new_node#to make tail also pointing to new node.as it is the 1st node.
        self.length = 1#for keeping track of length

 
my_linked_list = LinkedList(4)
#calling LinkedList class with value 4.
print(my_linked_list.head.value)
#printing value of first item inserted above.
#ABOVE PROGRAM GIVES VALUE OF DATA STORED IN LINKED LIST.

                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
