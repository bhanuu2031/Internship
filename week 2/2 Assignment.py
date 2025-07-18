class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, n):
        if self.head is None:
            raise Exception("Cannot delete from an empty list.")
        
        if n < 1:
            raise Exception("Index out of range.")
        
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(n - 2):
            if current.next is None:
                raise Exception("Index out of range.")
            current = current.next
        
        if current.next is None:
            raise Exception("Index out of range.")
        
        current.next = current.next.next


ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.print_list() 

ll.delete_node(3)
ll.print_list()  

try:
    ll.delete_node(5)
except Exception as e:
    print(e)  

try:
    ll.delete_node(0)
except Exception as e:
    print(e) 

try:
    empty_ll = LinkedList()
    empty_ll.delete_node(1)
except Exception as e:
    print(e)  