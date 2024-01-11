class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        myVowels = [char for char in s if char in vowels]
        
        p = len(myVowels) - 1
        result = list(s)
        
        for i in range(len(s)):
            if s[i] in vowels:
                result[i] = myVowels[p]
                p -= 1
        
        return ''.join(result)
