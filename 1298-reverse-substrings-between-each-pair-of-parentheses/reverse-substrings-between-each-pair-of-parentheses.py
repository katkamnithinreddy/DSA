class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        open_b=0
        close_b=0
        n=len(s)
        l=[x for x in s]
        for i in range(n):
            if s[i]=="(":
                stack.append(i)
            if s[i]==')':
                j=stack.pop() 
                s.replace(s[j:i],s[i:j:-1])
                l[j:i]=l[i:j:-1]
        ans=""
        for i in l:
            if i!="(" and i!=")":
                ans+=i
        return ans
        



             
        