from collections import deque

def floodFill(image, sr, sc, newColor, color):
    if sr >= len(image) or sc >= len(image[0]) or sr < 0 or sc < 0 or image[sr][sc] != color:
        return

    original_color = image[sr][sc]
    if original_color == newColor:
        return

    queue = deque([(sr, sc)])

    while queue:
        current_sr, current_sc = queue.popleft()
        image[current_sr][current_sc] = newColor

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            new_sr, new_sc = current_sr + direction[0], current_sc + direction[1]
            if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr][new_sc] == original_color:
                queue.append((new_sr, new_sc))

# Your Solution class remains the same
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        floodFill(image, sr, sc, newColor, image[sr][sc])
        return image


