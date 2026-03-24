"""Linked List implementation Module"""


class ListNode:
    """Linked List Node Class Impl"""

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Linked List Class Impl"""

    def __init__(self):
        """Create a new singly-linked list, initially empty."""
        self.head = None

    def prepend(self, data):
        """Insert a new element at the beginning (head) of the list."""
        new_node = ListNode(data=data, next_node=self.head)
        self.head = new_node

    def append(self, data):
        """Insert a new element at the end of the list."""
        new_node = ListNode(data=data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        # Iteratate throught the nodes to the end and add the new node
        while curr.next_node:
            curr = curr.next_node
        curr.next_node = new_node

    def display(self):
        """Print the data of all nodes in the list."""
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next_node
        print("None")
