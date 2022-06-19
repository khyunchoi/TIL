from copy import deepcopy

def solution(grid):
    answer = []
    N = len(grid)
    M = len(grid[0])
    dij = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = [[0 for _ in range(M)] for _ in range(N)]

    def dfs(depth, new_grid):

        if depth == q_cnt:
            a_cnt = 0
            b_cnt = 0
            c_cnt = 0
            for i in range(N):
                for j in range(M):
                    if new_grid[i][j] == "a":
                        a_cnt += 1
                    elif new_grid[i][j] == "b":
                        b_cnt += 1
                    elif new_grid[i][j] == "c":
                        c_cnt += 1

            check_flag = 0
            for i in range(N):
                for j in range(M):
                    if new_grid[i][j] == "a" and a_cnt == 1:
                        continue
                    if new_grid[i][j] == "b" and b_cnt == 1:
                        continue
                    if new_grid[i][j] == "c" and c_cnt == 1:
                        continue

                    if not check(i, j):
                        check_flag = 1
                        break
                if check_flag:
                    break
            
            if check_flag == 0:
                if new_grid not in answer:
                    answer.append(deepcopy(new_grid))
            return

        for i in range(N):
            for j in range(M):
                if new_grid[i][j] == "?" and not visited[i][j]:
                    new_grid[i][j] = "a"
                    dfs(depth+1, new_grid)
                    new_grid[i][j] = "b"
                    dfs(depth+1, new_grid)
                    new_grid[i][j] = "c"
                    dfs(depth+1, new_grid)
                    new_grid[i][j] = "?"

    def check(i, j):
        flag = 0
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if new_grid[i][j] == new_grid[ni][nj]:
                    flag = 1
                    break
        
        if flag:
            return True
        else:
            return False
    
    new_grid = [["" for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_grid[i][j] = grid[i][j]

    q_cnt = 0
    for i in range(N):
        for j in range(M):
            if new_grid[i][j] == "?":
                q_cnt += 1

    dfs(0, new_grid)
    
    return len(answer)


print(solution(["??b", "abc", "cc?"]))
# print(solution(["abcabcab","????????"]))
print(solution(["aa?"]))