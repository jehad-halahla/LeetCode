from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        myStack = [asteroids[0]]
        
        for i in range(1, len(asteroids)):
            current_asteroid = asteroids[i]
            
            while myStack and current_asteroid < 0 < myStack[-1]:
                if abs(current_asteroid) > myStack[-1]:
                    myStack.pop()
                elif abs(current_asteroid) == myStack[-1]:
                    myStack.pop()
                    break
                else:
                    break
            
            else:
                myStack.append(current_asteroid)
            

        return myStack
