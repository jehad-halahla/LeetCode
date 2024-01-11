class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+= 1
        return len(dict.values()) == len(set(dict.values()))