class Solution:
    def removeStars(self, s: str) -> str:
        myList =[]
        for i in s:
            if i == '*':
                myList.pop()
            else:
                myList.append(i)
        return ''.join(myList)
        
        