class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        graph=[0]*n 
        cnt=0
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                cnt+=1 
            graph[i]=cnt 
        return [graph[u]==graph[v] for u,v in queries]
            
        