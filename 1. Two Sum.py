# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
import math
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for num in nums:
        if target - num in nums:
            index_first  = nums.index(num)
            index_second = nums.index(target - num)
            if index_first == index_second:
                if num in nums[index_first+1:]:
                    index_second = nums.index(num, index_first+1)
                else:
                    continue

            return [index_first, index_second]


    return []


nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))