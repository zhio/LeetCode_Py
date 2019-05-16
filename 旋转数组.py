#方法1，将最后k个删掉，插入到前面

def rotate1(nums,k):
    lenth = len(nums)-1
    if lenth <1 or k<1:
        return
    for i in range(k):
        nums.insert(0,nums[lenth])
        del nums[lenth+1]
    return nums

def rotate2(nums,k):
    i = k % len(nums)
    nums[:] = nums[-i:]+nums[:-i]

ls = [1,2,3]
print(rotate2(ls,1))