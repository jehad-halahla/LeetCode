class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)
        
        if set1 != set2:
            return False
        
        myMap1 = {}
        myMap2 = {}
        
        for i in word1:
            myMap1[i] = myMap1.get(i, 0) + 1
        for i in word2:
            myMap2[i] = myMap2.get(i, 0) + 1
      
        l1 = sorted(myMap1.values())
        l2 = sorted(myMap2.values())
                
        return l1 == l2
