"""
- [How to sort a linked list using merge sort](https://www.educative.io/edpresso/how-to-sort-a-linked-list-using-merge-sort)
  - https://www.geeksforgeeks.org/merge-sort-for-linked-list/
  - https://www.interviewkickstart.com/learn/merge-sort-for-linked-list
"""

from typing import Tuple


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node|None = None

def merge_sort(root: Node) -> Node:
    """Merge Sort for a Linked List
    1. split list with fast/slow pointer iteration
    2. merge by looping through "left" and "right" lists and rearranging next pointers in sorted order
    3. recursively repeat
    """

    def merge(left: Node, right: Node) -> Node:
        root = left if left.data <= right.data else right
        left = root.next
        while left:
            left.next = left if left.data <= right.data else right
        

    def get_middle(root: Node) -> tuple[Node, Node]:
        slow = fast = root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        return (root, right)

    if root is None or root.next is None: return root

    l, r = get_middle(root)
    return merge(merge_sort(l), merge_sort(r))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
