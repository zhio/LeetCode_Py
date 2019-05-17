"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
def plusOne(digits):
    if len(digits) == 0:
        digits = [1]
    elif digits[-1] == 9:
        digits = plusOne(digits[:-1])
        digits.extend([0])
    else:
        digits[-1] += 1
    return digits
