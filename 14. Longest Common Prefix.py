# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs[0]) == 0:
        return ""
    smallest_str = strs[0]
    for string in strs:
        if len(string) < len(smallest_str):
            smallest_str = string

    while len(smallest_str) > 0:
        matches = True
        for string in strs:
            if not string.startswith(smallest_str):
                matches = False
        if not matches:
            smallest_str = smallest_str[:-1]
        else:
            return smallest_str

    return ""



test1 = ["flower","flow","flight"]
test2 = ["dog","racecar","car"]
test3 = ["ab", "a"]

print(longestCommonPrefix(test1))
print(longestCommonPrefix(test2))
print(longestCommonPrefix(test3))
