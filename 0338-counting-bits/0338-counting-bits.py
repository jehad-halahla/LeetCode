class Solution:
    def countBits(self, n: int) -> List[int]:
        print(2&1)
        myList = [0]*(n+1)
        for i in range(n+1):
            ans = 0
            for j in range(32):
                if i&(1<<j):
                    ans+=1
            myList[i] += ans
        return myList
                