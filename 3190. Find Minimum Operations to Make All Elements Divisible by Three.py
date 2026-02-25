# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums divisible by 3.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: 3
#
# Explanation:
#
# All array elements can be made divisible by 3 using 3 operations:
#
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
# Example 2:
#
# Input: nums = [3,6,9]
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

from typing import List


def minimumOperations(nums: List[int]) -> int:
    count_of_nums_not_divisible_by_three = 0
    for num in nums:
        if num % 3 != 0:
            count_of_nums_not_divisible_by_three = count_of_nums_not_divisible_by_three + 1

    return count_of_nums_not_divisible_by_three



test1 = [1,2,3,4]
test2 = [3,6,9]

print(minimumOperations(test1))
print(minimumOperations(test2))
