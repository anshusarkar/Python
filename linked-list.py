class LinkedList:
    def __init__(self, data=None): # Here data inputs dosen't have types !
        self.data = data
        self.next = None

    def insert(self, data):
        new_node = LinkedList(data) # Instance of Linkedlist class
        if self.next is None:
            self.next = new_node
        else:
            last_node = self.next
            while last_node.next is not None :
                last_node = last_node.next # This would incress the number of connected nodes thus incressing the total number of connected nodes
            last_node.next = new_node 
            # That code chunck starting from else block would                           
            # instantiate a new node connected with previous node for each call of insert method

    def display(self):
        current_node = self
        while current_node:                      # This method won't stop displaying the nodes until the self.next is None meaning it would be printing
            print(current_node.data, end=" -> ") # all the linked nodes
            current_node = current_node.next
        print("None")


llist = LinkedList(1)
llist.insert("cat")
llist.insert(3)

print("Linked list : ")
llist.display()
