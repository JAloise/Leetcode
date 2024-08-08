class Solution:
    def isPalindrome(x: int) -> bool:
        num = x 
        rev = 0
        if num < 0:
            return False
        elif num == 0:
            return True
            
        while num >= 0:#x=121
            rev = (rev*10) + (num % 10)
            num = num // 10
            if x == rev:
                return True
        
        
print(Solution.isPalindrome(121))