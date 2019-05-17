"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
def twoSum(nums,target):
    res = []
    for i,k in enumerate(nums):
        for j,kk in enumerate(nums[i+1:]):
            if k + kk == target:
                res.append(i)
                res.append(i+j+1)
    return res

def twoSum2(nums,target):
    n = len(nums)
    for x in range(n):
        b = target-nums[x]
        if b in nums:
            y = nums.index(b)
            if y != x:
                return x,y

def twoSum3(nums,target):
    n = len(nums)
    d = {}
    for x in range(n):
        a = target - nums[x]
        if nums[x] in d:
            return d[nums[x]],x
        else:
            d[a] = x

print(twoSum([3,2,4],6))