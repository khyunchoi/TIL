from collections import deque

def solution(city):
    dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[0 for _ in range(len(city[0]))] for _ in range(len(city))]
    q = deque()
    for i in range(len(city)):
        for j in range(len(city[0])):
            if city[i][j] == 0:
                visited[i][j] = 1
                q.append((i, j, 0))

    while q:
        pi, pj, ptmp = q.popleft()

        for di, dj in dij:
            ni = pi + di
            nj = pj + dj

            if 0 <= ni < len(city) and 0 <= nj < len(city[0]) and not visited[ni][nj]:
                if city[ni][nj] != 0:
                    visited[ni][nj] = 1
                    city[ni][nj] = ptmp+1
                    q.append((ni, nj, ptmp+1))

    return city