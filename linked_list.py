class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        current = self.head
        if not self.head:
            self.head = Node(data)
            return
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def get_tail_data(self):
        current = self.head
        while current.next_node:
            current = current.next_node
        return current.data
