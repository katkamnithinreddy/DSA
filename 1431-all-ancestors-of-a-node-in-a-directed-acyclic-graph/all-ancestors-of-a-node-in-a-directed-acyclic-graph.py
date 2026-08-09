class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import deque 
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[v].append(u)
        ans=[[] for _ in range(n)]
        def findans(node):
            queue=deque()
            visited = set()
            for it in graph[node]:
                queue.append(it)
                visited.add(it)
            while queue:
                x=queue.popleft()
                for i in graph[x]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i) 
            ans[node]=sorted(visited)
        for i in range(n):
            findans(i) 
        return ans



        