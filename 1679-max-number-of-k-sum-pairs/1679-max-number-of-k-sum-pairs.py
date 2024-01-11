class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #O(N*LOG N ) solution
        # sort the list
        nums.sort()
        l = 0
        r = len(nums)-1
        ans =0
        while l < r :
            if nums[l] + nums[r] == k:#must equalize 
                r -=1
                l +=1
                ans +=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return ans
        
        