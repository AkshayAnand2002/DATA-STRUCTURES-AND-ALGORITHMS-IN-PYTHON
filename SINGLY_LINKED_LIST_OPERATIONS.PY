class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
print('Menu')
print("WRITE THE FOLLOWING STATEMENTS WITH VALUES IN CORRECT PLACE.")
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
while True:
    print('The list: ', end = '')
    a_llist.display()
    print()
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_llist.insert_at_beg(new_node)
            elif position == 'end':
                a_llist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.insert_before(ref_node, new_node)
    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.remove(node)
    elif operation == 'quit':
        break
#output of the above code and how to give input ------>
----------------------------------------------------------------------------------------------------------
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 7 at beg
The list: 7 
What would you like to do? insert 3 at end
The list: 7 3 
What would you like to do? insert 1 after 0
The list: 7 1 3 
What would you like to do? insert 9 before 2
The list: 7 1 9 3 
What would you like to do? remove 2
The list: 7 1 3 
What would you like to do? insert 12 at end
The list: 7 1 3 12 
What would you like to do? remove 0
The list: 1 3 12 
What would you like to do? quit
----------------------------------------------------------------------------------------------------------
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 5 after 0
No such index.
The list: 
What would you like to do? insert 3 at end
The list: 3 
What would you like to do? insert 1 after 0
The list: 3 1 
What would you like to do? insert 2 before 1
The list: 3 2 1 
What would you like to do? insert 0 at end
The list: 3 2 1 0 
What would you like to do? remove 3
The list: 3 2 1 
What would you like to do? remove 2
The list: 3 2 
What would you like to do? quit
-----------------------------------------------------------------------------------------------------------
