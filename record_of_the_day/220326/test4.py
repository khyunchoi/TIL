def solution(n, edges):
    answer = 0
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for i, j in edges:
        arr[i][j] = 1
        arr[j][i] = 1
    
    
    def dfs(i, cnt):
        if counts[i] == 0:
            counts[i] = cnt
        
        for j in range(n):
            if not visited[j] and arr[i][j] == 1:
                visited[j] = 1
                dfs(j, cnt+1)


    for i in range(n):
        counts = [0 for _ in range(n)]
        visited = [0 for _ in range(n)]
        visited[i] = 1
        dfs(i, 0)
        answer += sum(counts) - (n - 1)

    return answer


print(solution(5, [[0,1],[0,2],[1,3],[1,4]]))
print(solution(4, [[2,3],[0,1],[1,2]]))