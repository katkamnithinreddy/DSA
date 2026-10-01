class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] 
        hashh={")":"(","]":"[","}":"{"}
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i) 
            else:
                if stack==[]:
                    return False 
                if stack[-1]==hashh[i]:
                    stack.pop()
                else:
                    return False
        if stack==[]:
            return True 
        return False
        