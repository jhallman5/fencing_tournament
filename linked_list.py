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
        ''' Creates a Node from provided data and inserts it into the sorted LL. '''
        node_to_sort = Node(data)
        if not self.head:
            self.head = node_to_sort
            return
        current = self.head
        if self.is_new_node_higher_rank(current, node_to_sort):
            node_to_sort.set_next(current)
            self.head = node_to_sort
            return
        while True:
            if not current.next_node:
                current.set_next(node_to_sort)
                break
            if self.is_new_node_higher_rank(current.next_node, node_to_sort):
                node_to_sort.set_next(current.next_node)
                current.set_next(node_to_sort)
                break
            else:
                current = current.next_node


    def print_LL(self):
        '''Print LL for development'''
        print('------------------')
        current = self.head
        print(current.data)
        while current.next_node:
            current = current.next_node
            print(current.data)

    def get_tail_data(self):
        current = self.head
        while current.next_node:
            current = current.next_node
        return current.get_data

    def is_new_node_higher_rank(self, current, new_node):
        ''' Compares letter rank and year rank. '''
        if self.get_letter_rank(new_node) > self.get_letter_rank(current):
            return True
        if self.get_letter_rank(new_node) == self.get_letter_rank(current):
            if self.get_year_rank(new_node) >= self.get_year_rank(current):
                return True
        return False

    def get_letter_rank(self, node):
        ''' Function to assign letter rank values. '''
        letter_rank = node.data.get('rank')[0]
        return {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1,
            'U': 0
        }[letter_rank]

    def get_year_rank(self, node):
        ''' Returns year only rank. '''
        return node.data.get('rank')[1:]
