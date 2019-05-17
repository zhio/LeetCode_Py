"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""
def isValidsudoku(board):
    Row,Col,Grid = [''] * 9,['']*9,['']*9

    for r_index,row in enumerate(board):
        for c_index,ch in enumerate(row):
            g_index = r_index // 3 *3 + c_index //3
            if ch != '.':
                if ch in Row[r_index] or ch in Col[c_index] or ch in Grid[g_index]:
                    return False
                Row[r_index] += ch
                Col[c_index] += ch
                Grid[g_index] += ch

    return True