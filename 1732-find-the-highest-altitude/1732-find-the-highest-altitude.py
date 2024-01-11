class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]*(len(gain)+1)
        maxPre = prefix[0]
        for i in range(len(gain)):
            prefix[i+1] = prefix[i] + gain[i]
            maxPre = max(maxPre,prefix[i+1])
        return maxPre