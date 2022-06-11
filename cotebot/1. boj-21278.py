# https://www.acmicpc.net/problem/21278
n, m = map(int, input().split())
mx = 10000000000
graph = [[mx] * (n + 1) for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = b
    graph[b] = a

for i in graph:
    print(i)