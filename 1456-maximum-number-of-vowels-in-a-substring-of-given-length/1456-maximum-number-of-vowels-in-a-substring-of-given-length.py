class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        # Initial window number of vowels
        ans = 0
        for i in range(0, k):
            if s[i] in vowels:
                ans += 1
        maxAns = ans
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                ans -= 1
            if s[i + k - 1] in vowels:
                ans += 1
            maxAns = max(maxAns, ans)

        return maxAns  # Corrected return statement
