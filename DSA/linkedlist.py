class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as null

    # Method to add a new node at the end of the list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

llist.print_list()
