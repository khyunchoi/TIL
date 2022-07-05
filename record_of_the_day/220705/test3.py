from pprint import pprint
import sys
sys.setrecursionlimit(50000000)

def solution(rows, columns, lands):
    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    min_result = rows*columns
    max_result = 0
    dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def sea_dfs(i, j):
        board[i][j] = 2

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < rows and 0 <= nj < columns and board[ni][nj] == 0:
                sea_dfs(ni, nj)

    
    def lake_dfs(i, j):
        if board[i][j] == 0:
            size[0] += 1
            board[i][j] = 3

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < rows and 0 <= nj < columns and board[ni][nj] == 0:
                lake_dfs(ni, nj)


    for land in lands:
        board[land[0]-1][land[1]-1] = 1

    sea_dfs(0, 0)

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 0:
                size = [0]
                lake_dfs(i, j)
                min_result = min(min_result, size[0])
                max_result = max(max_result, size[0])
    
    if max_result == 0:
        min_result = -1
        max_result = -1
    answer.append(min_result)
    answer.append(max_result)

    return answer


print(solution(9,7,[[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3], [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]]))
print(solution(5,6,[[2, 2], [2, 3], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]))
print(solution(5,7,[[2, 5], [3, 3], [3, 4], [3, 5], [4, 3]]))