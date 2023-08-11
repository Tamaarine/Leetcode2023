from typing import *
from collections import *


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(edges, visited, current, destination):
            if current == destination:
                return True

            # Mark the current node as visited
            visited[current] = True

            # First find the incident edges of the current node
            for incidentNode in graph[current]:
                if not visited[incidentNode]:
                    if dfs(edges, visited, incidentNode, destination):
                        return True
            return False

        visited = [False for _ in range(n + 1)]
        return dfs(edges, visited, source, destination)


class Solution2:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque()
        queue.append(source)

        visited = [False for _ in range(n + 1)]

        while queue:
            currentNode = queue.popleft()
            visited[currentNode] = True

            if currentNode == destination:
                return True

            incidentEdges = graph[currentNode]
            for edge in incidentEdges:
                if not visited[edge]:
                    # Mark it as visited because you will be appending it into the queue.
                    visited[edge] = True
                    queue.append(edge)

        return False


s = Solution2()
print(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
print(
    s.validPath(
        10,
        [
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        5,
        9,
    )
)
