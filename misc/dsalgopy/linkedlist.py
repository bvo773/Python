class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print("[ {} ] ->".format(curr_node.data), end="")
            curr_node = curr_node.next

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if (self.head.next is None):
            self.tail = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if (self.tail is None):
            self.tail = new_node
        elif (self.tail.next is None):
            self.tail.next = new_node
            self.tail = new_node
        if (self.head is None):
            self.head = new_node

    def reverse_list(self):
        pass

    def delete_node(self):
        pass
# node1 = Node(1)
# node2 = Node(2)


singly_linked_list = SinglyLinkedList()
singly_linked_list.insert_head(1)
singly_linked_list.insert_head(2)
singly_linked_list.insert_head(3)
singly_linked_list.insert_tail(5)


singly_linked_list.print_list()
