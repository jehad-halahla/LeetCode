class Solution:
    def intToRoman(self, num: int) -> str:
        # IV = 5 - 1 = 4 and a pattern can be noted....
        myDict = {1000: "M", 900: "CM",
          500: "D", 400: "CD",
          100: "C", 90: "XC",
          50: "L", 40: "XL",
          10: "X", 9: "IX",
          5: "V", 4: "IV",
          1: "I"
          }
        res = ""
        for i in myDict.keys():
            itt = num//i
            num %= i
            res += myDict[i]*itt
        return res