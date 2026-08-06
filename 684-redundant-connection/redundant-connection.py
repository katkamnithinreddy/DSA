class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        def find(x):
            while parent[x]!=x:
                x=parent[x] 
            return x 
        def union(u,v):
            pu,pv=find(u),find(v) 
            if pu==pv:
                return False 
            parent[pu]=pv
            return  True
        for u,v in edges:
            if not union(u,v):
                return [u,v]

                

        