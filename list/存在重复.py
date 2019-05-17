"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""
def containsDuplicate(nums):
    print(len(nums))
    print(len(set(nums)))
    return len(nums) != len(set(nums))

a = [1,2,3,1]
print(containsDuplicate(a))

def containsDuplicate2(nums):
    for i in nums:
        if nums.cout(i)>=2:
            return True

    return False