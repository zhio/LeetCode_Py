"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""
def moveZeroes(nums):
    res = 0
    i = 0
    while i <len(nums):
        if nums[i] == 0:
            del nums[i]
            res +=1
            continue
        i +=1
    while res>0:
        nums.extend([0])
        res -=1

    return nums

print(moveZeroes([0,0,1]))