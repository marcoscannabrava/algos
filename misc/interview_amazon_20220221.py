# Output: ((((a+b)*c)+d)-e)
# Input: 
#             -
#            /  \
#         +    e
#         / \
#       *  d
#     /  \
#    +  c 
#  / \
# a   b 

# Can you write a method/function that given an instance of your Node/Tree class, 
# returns the (infix) expression its tree represents? For example, if I gave the tree I drew on the board, 
# I'd want it to return the expression you said that represents.

"""
> approach #1: DFS in-order traversal of tree

Example:
Input: node = Node('-')
Output: "((((a+b)*c)+d)-e)"

DFS(Node('+'))
-> "(" + DFS(Node('a')) + root.value + DFS(Node('a')) + ")"

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def DFS(root, result=None):
    if result is None:
        result = ""
    if root.left is None and root.right is None:
        return root.value
    return f"({DFS(root.left, result)}{root.value}{DFS(root.right, result)})"
