# Palindrome
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[\W_]+')
        t = regex.sub('', s).lower()
        length = len(t)
        for i in range(length // 2):
            if t[0+i] != t[length-i-1]:
                return False
        return True

# Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def maxDepthRecursive(self, root):
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)
    def maxDepth(self, root):
        if root is None: return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            nodes_in_level = len(queue)
            while nodes_in_level:
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                nodes_in_level -= 1
        return depth



