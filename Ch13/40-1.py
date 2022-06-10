# https://leetcode.com/problems/network-delay-time/
# 514ms 16.5MB
import heapq


class Solution:
    @staticmethod
    def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        mx = 1000000000
        graph, distance = [[] for _ in range(n + 1)], [mx] * (n + 1)

        for i in times:
            a, b, time = map(int, i)
            graph[a].append((b, time))

        def dijkstra(start):
            q = []
            # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
            heapq.heappush(q, (0, start))
            distance[start] = 0
            while q:
                # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
                dist, now = heapq.heappop(q)
                # 현재 노드가 이미 저리된 적이 있는 노드라면 무시
                if distance[now] < dist:
                    continue
                # 현재 노드와 연결된 다른 인접한 노드들을 확인
                for i in graph[now]:
                    cost = dist + i[1]
                    # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))
        dijkstra(k)
        result = max(distance[1:])
        if result == mx:
            result = -1
        return result