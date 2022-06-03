# https://leetcode.com/problems/number-of-islands/
# 346ms 16.3MB
from collections import deque


class Solution:
    @staticmethod
    def numIslands(grid: list[list[str]]) -> int:
        dx, dy, count = [1, -1, 0, 0], [0, 0, 1, -1], 0

    # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = "0"
            # 큐가 빌때까진 반복
            while queue:
                x, y = queue.popleft()
                # 4방향 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                        continue
                    # 방문한경우
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count = count + 1
        return count
