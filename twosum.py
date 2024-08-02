from typing import List

#Force Brute Algo O(n)
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