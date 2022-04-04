def solution(n, edges, k, a, b):
    board = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0 for _ in range(n)]
    line_set = set()

    for edge in edges:
        i, j = edge
        board[i][j] = 1
        board[j][i] = 1
    
    def dfs(start, way, depth):
        if depth > k:
            return

        if start == b:
            for i in range(len(way)-1):
                line_set.add((min(way[i], way[i+1]), max(way[i], way[i+1])))
            return

        for i in range(len(board)):
            if board[start][i] == 1 and not visited[i]:
                visited[i] = 1
                dfs(i, way+[i], depth+1)
                visited[i] = 0
                
    visited[a] = 1
    dfs(a, [a], 0)
    
    return len(line_set)

print(solution(8, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3))