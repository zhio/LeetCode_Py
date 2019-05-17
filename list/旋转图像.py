"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""
def rotate(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i+1,length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]