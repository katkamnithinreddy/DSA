class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hashmap={} 
        for i in knowledge:
            hashmap[i[0]]=i[1] 
        inside=0
        ans=""
        keyy=""
        for i in s:
            if i=="(":
                inside=1 
            elif i==")":
                inside=0 
                if keyy in hashmap:
                    ans+=hashmap[keyy] 
                else:
                    ans+="?"
                keyy=""
            elif inside:
                keyy+=i 
            else:
                ans+=i 
        return ans
            


            

        