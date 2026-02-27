# We have two special characters:
#
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
#
# Example 1:
#
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:
#
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
#
# Constraints:
#
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.

from typing import List

def isOneBitCharacter(bits: List[int]) -> bool:
    in_char = False
    i = 0
    while i < len(bits):
        if bits[i] == 1: #anytime we see a 1 we know it will be 10 or 11 so skip it and keep it known
            in_char = True
            i += 2
        else: #this means it is a 0, the special char 10 or 11 does not start with 0
            in_char = False
            i +=1
    return not in_char



bits1 = [1,0,0]
bits2 = [1,1,1,0]
bits3 = [0,0]
bits4 = [1,1,1,1,1,1,0]
bits5 = [0,1,0]
bits6 = [0,0,1,0]

print(isOneBitCharacter(bits1))
print(isOneBitCharacter(bits2))
print(isOneBitCharacter(bits3))
print(isOneBitCharacter(bits4))
print(isOneBitCharacter(bits5))
print(isOneBitCharacter(bits6))
