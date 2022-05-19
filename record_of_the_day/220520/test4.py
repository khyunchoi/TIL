def solution(grid):
    answer = -1
    N = len(grid)
    M = len(grid[0])
    dij = ((-1, 0), (0, 1), (1, 0), (0, -1))
    grids = []

    def make_grid():
        pass

    def check(i, j):
        flag = 0
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if grid[i][j] == grid[ni][nj]:
                    flag = 1
                    break
        
        if flag:
            return True
        else:
            return False

    return answer

    
print(solution(["??b", "abc", "cc?"]))
print(solution(["abcabcab","????????"]))
print(solution(["aa?"]))