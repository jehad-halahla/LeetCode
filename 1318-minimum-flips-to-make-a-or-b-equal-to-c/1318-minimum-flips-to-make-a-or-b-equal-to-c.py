class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(33):
            aBit = (a>>i)&1
            bBit = (b>>i)&1
            cBit = (c>>i)&1
            if aBit == 1 and bBit == 1 and cBit == 0:
                flips+=2
            elif aBit== 0 and bBit == 0 and cBit ==1:
                flips+=1
            elif aBit^bBit == 1 and cBit == 0:
                flips+=1
        return flips
            