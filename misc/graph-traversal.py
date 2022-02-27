# BFS traversal from a given source vertex.
from collections import defaultdict, deque
# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [s]
        queue = deque([s])
        while queue:
            s = queue.popleft()
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

# -----------------------------------------

# DFS traversal from a given source vertex.
class DFS(Graph):
    def drill_down(self, s, visited):
        visited.append(s)
        for n in self.graph[s]:
            if n not in visited:
                self.drill_down(n, visited)

    def DFS_recursive(self, s):
        visited = []
        self.drill_down(s, visited)

    def DFS(self, s):
        stack = [s]
        visited = []
        while stack:
            s = stack.pop()
            visited.append(s)
            for n in self.graph[s]:
                if n not in visited:
                    stack.append(s)
