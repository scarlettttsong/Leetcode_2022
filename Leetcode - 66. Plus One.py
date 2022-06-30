"""
Leetcode - 66. Plus One
Lintcode - 407 · 加一

给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
"""

digits = [1, 2, 3]


def plusOne(digits):
    string = ""
    for i in range(len(digits)):
        string = string + str(digits[i])
        ans = int(string)+1
        result = [int(c) for c in str(ans)]
    print(result)


plusOne(digits)


