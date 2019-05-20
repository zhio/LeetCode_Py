"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
"""
def firstUniqChar(s):
    length = len(s)
    for i in range(length):
        for j in range(length):
            if s[i] == s[j] and i != j:
                break
            elif j == length-1:
                return i
    return -1

def firstUniqChar2(s):
    number = []
    dic = {}
    for i in range(len(s)):
        if s[i] not in number:
            number.append(s[i])
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1

    for j in range(len(number)):
        if dic.get(number[j]) == 1:
            for k in range(len(s)):
                if s[k] == number[j]:
                    return k
    return -1