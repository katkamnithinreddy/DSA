class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        l=[]
        def func(i,j):
            if i==n and j==n:
                ans.append("".join(l.copy()))
                return l
            if i<n:
                l.append("(")
                func(i+1,j) 
                l.pop()
            if j<n:
                if l!=[] and i>j:
                    l.append(")") 
                    func(i,j+1) 
                    l.pop()
            return l 
        func(0,0)
        return ans
        