# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Reference to the next node

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Starting with an empty list

    # Method to append data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse till the end
            last_node = last_node.next
        last_node.next = new_node

    # Method to print the list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist.print_list()  # Expected output: 1 -> 2 -> 3 -> 4 -> None
