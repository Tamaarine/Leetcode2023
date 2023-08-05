from typing import *
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Counting fresh oranges and putting rottens ones into queue
        freshCount = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j))
                elif val == 1:
                    freshCount += 1

        time = 0
        # Now based off from the rotten orange queue, we are going to perform
        # a breadth-first search to rotten all the neighboring oranges
        # Also if the freshCount is none break early, so we don't need to process those rotten oranges still in queue
        while len(queue) != 0 and freshCount > 0:
            # We are going to rot all the neighboring of the rotten oranges within the queue
            time += 1

            # Within the while loop we want to examine ALL of the rotten oranges
            # within this time slot, before proceeding to the next
            len_queue = len(queue)

            for _ in range(len_queue):
                rot_i, rot_j = queue.popleft()

                row_combo = [1, 0, -1, 0]
                col_combo = [0, 1, 0, -1]

                for row, col in zip(row_combo, col_combo):
                    new_row = rot_i + row
                    new_col = rot_j + col

                    # The orange that we are looking at are out of bound
                    # or it is empty or it is already rotten which means it is already in the queue
                    if (
                        new_row < 0
                        or new_row >= len(grid)
                        or new_col < 0
                        or new_col >= len(grid[0])
                        or grid[new_row][new_col] == 0
                        or grid[new_row][new_col] == 2
                    ):
                        continue

                    # Fresh orange that needs to be rotten
                    grid[new_row][new_col] = 2
                    freshCount -= 1

                    # Add this newly rotten orange into the queue
                    queue.append((new_row, new_col))
        if freshCount == 0:
            return time
        return -1


s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))
