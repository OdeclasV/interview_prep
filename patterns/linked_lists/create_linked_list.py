### Create a linked list

from __future__ import print_function

class Node:
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)