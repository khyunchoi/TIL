def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    dij = [[0, 1], [1, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]

    ni, nj = 0, 0
    tmp = 2
    answer[ni][nj] = 1

    if horizontal:
        direction = 0
    else:
        direction = 3

    for x in range(1, n):
        for y in range(direction, direction+3):
            if y == 0 or y == 3:
                ni += dij[y][0]
                nj += dij[y][1]

                answer[ni][nj] = tmp
                tmp += 1
            else:
                for _ in range(x):
                    ni += dij[y][0]
                    nj += dij[y][1]

                    answer[ni][nj] = tmp
                    tmp += 1
            
            direction = (direction + 3) % 6

    return answer


print(solution(4, True))
print(solution(5, False))