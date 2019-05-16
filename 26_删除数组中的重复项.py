#思路：
#判断数组中第i位和第i+1位是否相同，如果相同，就删除掉第i位，否则就将i+1，最后输出nums的长度
def removeDuplicates(nums):
    i = 0
    while i<len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        else:
            i+=1

    return len(nums)

numss = [0,0,1,1,1,2,2,3,3,4]

a = removeDuplicates(numss)
print(a)