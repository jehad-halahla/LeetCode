class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if not i % 2:
                res = res + word1[p1]
                p1 += 1
            else:
                res = res + word2[p2]
                p2 += 1
            i += 1
        if len(word1) > len(word2):
            res = res + word1[p1:]
        else:
            res = res + word2[p2:]
        return res
