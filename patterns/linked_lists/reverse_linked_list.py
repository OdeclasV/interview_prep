### Reverse linked list


class Node:
    # create linked list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    # print linked list values
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
    
    # reverse linked list
    def reverse(head):
        previous, current, next = None, head, None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)

result = Node.reverse(head)
Node.print_list(result)