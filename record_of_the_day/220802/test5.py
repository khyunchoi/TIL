def solution(grids):
    answer = []
    for grid in grids:
        n = len(grid)
        m = len(grid[0])
        b_start_i, b_start_j = 0, 0
        b_end_i, b_end_j = 0, 0
        w_start_i, w_start_j = 0, 0
        w_end_i, w_end_j = 0, 0

        flag = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    flag = 1
                    b_start_i, b_start_j = i, j
                    break
            if flag:
                break
        
        for i in range(b_start_i, n):
            if grid[i][b_start_j] == '.':
                b_end_i = i - 1
                break
        else:
            b_end_i = n - 1

        for j in range(b_start_j, m):
            if grid[b_start_i][j] == '.':
                b_end_j = j - 1
                break
        else:
            b_end_j = m - 1

        flag = 0
        for i in range(b_start_i, b_end_i+1):
            for j in range(b_start_j, b_end_j+1):
                if grid[i][j] == '.':
                    flag = 1
                    w_start_i, w_start_j = i, j
                    break
            if flag:
                break
        else:
            answer.append(False)
            continue

        for i in range(w_start_i, b_end_i+1):
            if grid[i][w_start_j] == 'X':
                w_end_i = i - 1
                break

        for j in range(w_start_j, b_end_j+1):
            if grid[w_start_i][j] == 'X':
                w_end_j = j - 1
                break
        
        answer_flag = 0
        for i in range(n):
            for j in range(m):
                if w_start_i <= i <= w_end_i and w_start_j <= j <= w_end_j:
                    if grid[i][j] == 'X':
                        answer_flag = 1
                        break
                elif b_start_i <= i <= b_end_i and b_start_j <= j <= b_end_j:
                    if grid[i][j] == '.':
                        answer_flag = 1
                        break
                else:
                    if grid[i][j] == 'X':
                        answer_flag = 1
                        break
            if answer_flag:
                break
        
        if answer_flag:
            answer.append(False)
        else:
            answer.append(True)

    return answer







print(solution([[".....",".XXX.",".X.X.",".XXX.","....."],["XXXXX","XXXXX","XXX.X","XXX.X","XXXXX"],["XXXXX","X...X","X.X.X","X...X","XXXXX"],["....X",".....","XXX..","X.X..","XXX.."],[".......","XXX.XXX","X.X.X.X","XXX.XXX","......."],["XXXXX","XX.XX","X...X","XX.XX","XXXXX"]]))