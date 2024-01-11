from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0

        while i < length:
            if flowerbed[i] == 0:
                # Check if the current position and its neighbors are all empty
                is_empty = (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0)
                if is_empty:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1
                    i += 2  # Move two steps ahead to avoid adjacent planted flowers
                else:
                    i += 1  # Move to the next position
            else:
                i += 2  # Skip the next position, as it is occupied

        return n <= 0
