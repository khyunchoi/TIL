def solution(n, paths, gates, summits):
    answer_list = []
    intensity_list = [10000000]
    board = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for path in paths:
        board[path[0]][path[1]] = path[2]
        board[path[1]][path[0]] = path[2]


    def dfs(now, intensity):
        if intensity > intensity_list[0]:
            return

        if now in summits:
            if intensity_list[0] == intensity:
                answer_list.append([now, intensity])
            elif intensity_list[0] > intensity:
                intensity_list[0] = intensity
                answer_list.clear()
                answer_list.append([now, intensity])
            return

        for next in range(1, n+1):
            if not visited[next] and board[now][next] and board[now][next] <= intensity_list[0]:
                visited[next] = 1
                dfs(next, max(intensity, board[now][next]))
                visited[next] = 0


    for i in range(len(gates)):
        visited = [0 for _ in range(n+1)]
        for j in range(len(gates)):
            visited[gates[j]] = 1

        dfs(gates[i], 0)

    answer_list.sort(key=lambda x: x[0])
    return answer_list[0]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))