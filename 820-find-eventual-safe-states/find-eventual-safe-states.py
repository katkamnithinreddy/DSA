class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        outdeg=[0]*n 
        rev = [[] for _ in range(n)]
        for u in range(n):
            outdeg[u] = len(graph[u])
            for v in graph[u]:
                rev[v].append(u)
        q = deque()

        for i in range(n):
            if outdeg[i] == 0:
                q.append(i)
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev[node]:
                outdeg[prev] -= 1
                if outdeg[prev] == 0:
                    q.append(prev)
        return [i for i in range(n) if safe[i]]
        
        