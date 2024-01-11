from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Handle the case where flowerbed has only one element
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n == 0

        for i in range(len(flowerbed)):
            # Check if the current position is suitable for planting
            if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0) and flowerbed[i] == 0:
                flowerbed[i] = 1  # Plant a flower
                n -= 1

        return n <= 0
