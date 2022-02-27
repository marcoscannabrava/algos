from LinkedList import Node
"""reverse linked list
:params head

> approach #1: keep previous pointer and point back as you iterate
"""

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev

def print_list(node):
    list = []
    while node:
        list.append(node.value)
        node = node.next
    print(list)

test = [Node(i) for i in range(6)]
for i, v in enumerate(test):
    test[i].next = test[i+1] if i < len(test) - 1 else None

head = test[0]
print('input')
print_list(head)
node = reverse_linked_list(head)
print('output')
print_list(node)

