from collections import deque

def solution(macaron):
    answer = []
    board = [[0 for _ in range(6)] for _ in range(6)]
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def down_left():
        for i in range(6):
            while 0 in board[i]:
                board[i].remove(0)
            while len(board[i]) < 6:
                board[i].append(0)


    def is_remove(x, y):
        tmp_list = [(x, y)]
        color = board[x][y]
        queue = deque()
        queue.append((x, y))
        visited = [[0 for _ in range(6)] for _ in range(6)]

        while queue:
            cx, cy = queue.popleft()
            visited[cx][cy] = 1

            for dx, dy in dxy:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < 6 and 0 <= ny < 6 and not visited[nx][ny]:
                    if board[nx][ny] == color:
                        tmp_list.append((nx, ny))
                        queue.append((nx, ny))

        return tmp_list


    for maca in macaron:
        line, color = maca[0] - 1, maca[1]
        for j in range(6):
            if board[line][j] == 0:
                board[line][j] = color
                break
        
        while True:
            remove_set = set()
            for i in range(6):
                for j in range(6):
                    if board[i][j] != 0:
                        tmp_remove_list = is_remove(i, j)
                        if len(tmp_remove_list) >= 3:
                            for item in tmp_remove_list:
                                remove_set.add(item)

            if len(remove_set) == 0:
                break

            remove_list = list(remove_set)
            for item in remove_list:
                board[item[0]][item[1]] = 0
            down_left()

    for j in range(5, -1, -1):
        tmp = ''
        for i in range(6):
            tmp += str(board[i][j])
        answer.append(tmp)

    return answer


print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]))
print(solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]))