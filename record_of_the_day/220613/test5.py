def solution(rc, operations):
    row = len(rc)
    col = len(rc[0])
    answer = [[0 for _ in range(col)] for _ in range(row)]

    def onRotate(i, j):
        if i == 0 or j == 0 or i == len(rc)-1 or j == len(rc[0])-1:
            return True
        return False

    for i in range(row):
        for j in range(col):
            tmp_i, tmp_j = i, j
            for operation in operations:
                if operation == 'ShiftRow':
                    if tmp_i == row - 1:
                        tmp_i = 0
                    else:
                        tmp_i += 1
                elif onRotate(tmp_i, tmp_j):
                    if tmp_i == 0 and 0 <= tmp_j < col - 1:
                        tmp_j += 1
                    elif tmp_i == row - 1 and 0 < tmp_j <= col - 1:
                        tmp_j -= 1
                    elif 0 <= tmp_i < row - 1 and tmp_j == col - 1:
                        tmp_i += 1
                    elif 0 < tmp_i <= row - 1 and tmp_j == 0:
                        tmp_i -= 1
                
            answer[tmp_i][tmp_j] = rc[i][j]

    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))