"""invert a binary tree
:params root

> approach #1: bfs while swapping children

https://leetcode.com/problems/invert-binary-tree/
"""

def invert_bt(root):
    visited = [root]
    while visited:
        node = visited.pop()
        if node is not None:
            visited += [node.right, node.left]
            node.left, node.right = node.right, node.left
    return root