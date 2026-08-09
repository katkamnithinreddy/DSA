class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        graph=[[] for _ in range(n)]
        indegree=[0]*n
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        ancestors=[set() for _ in range(n)]
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        while q:
            u=q.popleft()
            for v in graph[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        ans=[]
        for i in queries:
            if i[1] in ancestors[i[0]]:
                ans.append(True) 
            else:
                ans.append(False)
        return ans        