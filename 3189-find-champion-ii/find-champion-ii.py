class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg=[0]*n
        for u,v in edges:
            indeg[v]+=1 
        cham=-1 
        for i in range(n):
            if indeg[i]==0:
                if cham!=-1:
                    return -1 
                cham=i 
        return cham
        
        
         