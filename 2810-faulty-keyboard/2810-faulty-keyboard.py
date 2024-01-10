class Solution:
    def finalString(self, s: str) -> str:
        counter = 0 
        res = ""
        for i in s:
            if i == "i":
                res = res[::-1]
            else:
                res += i
        return res