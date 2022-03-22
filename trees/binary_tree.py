from BinaryTree import Node
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


"""104. Maximum Depth of Binary Tree
> approach #1: dfs keeping track of max_h

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


def max_depth(root):
    h = max_h = 0
    stack: list[tuple[Node | None, int]] = [(root, h)]
    while stack:
        node = stack.pop()
        if node[0]:
            h = node[1] + 1
            stack += [(node[0].left, h), (node[0].right, h)]
        else:
            if node[1] > max_h: max_h = node[1]
    return max_h


"""
Count Unival Trees

> example:
Input: root of below tree
L0              5
               / \
L1            4   5
             / \   \
L2          4   4   5                
Output: 5

> rundown:
unival_subtrees = 5
L0-5
left  = True, 4
right = True, 5
is_unival_subtree = False

L1-4                        L1-5
left  = True, 4             left  = True, None
right = True, 4             right = True, 5
is_unival_subtree = True    is_unival_subtree = True

L2-4                        L2-4                        L2-5
left  = True, None          left  = True, None          left  = True, None
right = True, None          right = True, None          right = True, None
is_unival_subtree = True    is_unival_subtree = True    is_unival_subtree = True


"""

def count_unival_subtrees(root):
    unival_subtrees = 0

    def dfs(node):
        left = right = (True, None)
        if node.left: left = dfs(node.left), node.left.value
        if node.right: right = dfs(node.right), node.right.value

        is_unival_subtree = left[0] and right[0] and (node.value == left[1] == right[1] or (node.value == left[1] and right[1] is None) or (node.value == right[1] and left[1] is None))
        if is_unival_subtree: unival_subtrees += 1
        
        return is_unival_subtree

    dfs(root)

    return unival_subtrees

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
def is_common_ancestor(curr, l, r):
    if l and r: return True
    if l and curr: return True
    if r and curr: return True
    return False
  
def common_ancestor(root=None, p, q):
    lca = None
    
    def dfs(node):
        if lca is not None: return False
        is_p_or_q = [p, q].includes(node.value)  # type: ignore
        if not node.left and not node.right:
            return is_p_or_q
        
        l: bool = dfs(node.left) if node.left else False
        r: bool = dfs(node.right) if node.right else False
        
        if is_common_ancestor(is_p_or_q, l, r): lca = node
        
        return (l OR r OR is_p_or_q)

    dfs(lca)
    return lca
