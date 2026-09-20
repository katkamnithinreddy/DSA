class Solution:
    def reverseDegree(self, s: str) -> int:
        summ=0
        for i in range(len(s)):
            summ+=((i+1)*ord(chr(123-ord(s[i]))))
        return summ
        