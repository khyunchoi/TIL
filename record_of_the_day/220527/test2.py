def solution(n, m, rectangle):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(m)]


    def check(x, y, length):
        for i in range(x, x+length):
            if i >= m:
                return False
            if board[i][y] == 1:
                return False

        for j in range(y, y+length):
            if j >= n:
                return False
            if board[x][j] == 1:
                return False

        return True


    rectangle.sort()
    new_rectangle_list = []
    for i in range(len(rectangle)):
        for _ in range(rectangle[i][1]):
            new_rectangle_list.append(rectangle[i][0])

    for rect in new_rectangle_list:
        flag = 0
        for i in range(m):
            for j in range(n):
                if check(i, j, rect):
                    flag = 1
                    answer.append([j, i, rect])
                    for a in range(i, i+rect):
                        for b in range(j, j+rect):
                            board[a][b] = 1
                    break
            if flag:
                break

    return answer

print(solution(7, 8, [[2,2],[1,4],[3,2],[4,40]]))