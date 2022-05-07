### print elements of linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)

head.print_list()