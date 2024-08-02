#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.



from typing import List

#Brute Force Algo, O(n^2) complexity
class Solution:
    def __init__(self) -> None:
        pass
    
    def twoSum(nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


num = [3,2,4]   
target = 6    
print(Solution.twoSum(num,target))

#test case num = [2,7,11,15] target = 9 output = [0,1]