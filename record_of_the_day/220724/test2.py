def solution(board):
    answer = [0]
    visited = [0 for _ in range(len(board))]


    def dfs(depth, tmp):
        if depth >= len(board):
            answer[0] = max(answer[0], tmp)
            return

        for i in range(len(board)):
            if not visited[i]:
                visited[i] = 1
                dfs(depth+1, tmp + board[depth][i])
                visited[i] = 0


    dfs(0, 0)

    return answer[0]