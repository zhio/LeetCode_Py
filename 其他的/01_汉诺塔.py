
"""
将 N 个圆盘从左边柱子移动到右边柱子：

[递归的]将 N-1 个圆盘从左边柱子移动到中间柱子。
将最大的圆盘从左边柱子移动到右边柱子。
[递归的]将 N-1 个圆盘从中间柱子移动到右边柱子。
"""
def hanoi(height,left='left',right='right',middle='middle'):
    if height:
        hanoi(height-1,left,middle,right)
        print(left,'=>',right)
        hanoi(height-1,middle,right,left)

hanoi(3)