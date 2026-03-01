# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
#
# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
#
# Return the string after rearranging the spaces.
#
#
# Example 1:
#
# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
# Example 2:
#
# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
#
#
# Constraints:
#
# 1 <= text.length <= 100
# text consists of lowercase English letters and ' '.
# text contains at least one word.
from os.path import join
from typing import List
import math

def reorderSpaces(text: str) -> str:
    total_spaces = 0
    for char in text:
        if char == " ":
            total_spaces += 1

    words = text.split()
    final_words = []
    for word in words:
        if word == "":
            continue
        final_words.append(word)

    if len(final_words) == 1:
        return "".join(final_words) + (" " * total_spaces)

    left_over_spaces = total_spaces % (len(final_words) - 1)

    spaces_to_insert = math.floor(total_spaces / (len(final_words) - 1))
    for i in range(0,len(final_words) - 1 ):
        final_words[i] = final_words[i] + (" " * spaces_to_insert)



    return "".join(final_words) + (" " * left_over_spaces)

test1 = "  this   is  a sentence "
test2 = " practice   makes   perfect"
test3 = "a"
test4 = "  hello"
# print("<"+reorderSpaces(test1)+">")
# print("<"+reorderSpaces(test2)+">")
# print("<"+reorderSpaces(test3)+">")
print("<"+reorderSpaces(test4)+">")
