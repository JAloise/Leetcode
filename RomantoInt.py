class Solution(object):
    def romanToInt(s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}#declare dictionary
        number = 0
        for i in range(len(s)-1): 
            if roman[s[i]] < roman[s[i+1]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]
        number += roman[s[-1]] #takes the last one into consideration
        return number
        
print(Solution.romanToInt("III"))