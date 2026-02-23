from typing import List


def runningSum(nums: List[int]) -> List[int]:
    ret_list: List[int] = []
    for i in range(len(nums)):
        ret_list.append(nums[i])
        for j in range(i-1, -1, -1):
            ret_list[i] += nums[j]
    return ret_list


test1 = [3,1,2,10,1]

print(runningSum(test1))