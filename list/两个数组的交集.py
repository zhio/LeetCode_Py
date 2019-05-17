"""
给定两个数组，编写一个函数来计算它们的交集。

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
"""
import collections
def intersect(nums1,nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return res

def intersect2(nums1,nums2):
    a,b = map(collections.Counter,(nums1,nums2))
    return list((a&b).elements)