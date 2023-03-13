'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 '''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return i,j


# INSTANCE FOR THE CLASS
s = Solution()


#CALL TWO SUM
nums = [1,2,3,4]
target = 4
print(s.twoSum(nums, target))