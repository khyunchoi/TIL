def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    dij = ((0, 1), (1, 0), (0, -1), (-1, 0))


    def go(i, j, idx):
        standard = n-1
        tmp = 1

        while standard > 0:
            tmp_standard = standard

            while tmp_standard:
                di, dj = dij[idx]
                i += di
                j += dj

                if clockwise:
                    answer[i][j] = tmp
                else:
                    answer[j][i] = tmp
                tmp += 1
                tmp_standard -= 1

            idx = (idx + 1) % 4
            standard -= 2


    go(0, -1, 0)
    go(-1, n-1, 1)
    go(n-1, n, 2)
    go(n, 0, 3)

    if n % 2:
        answer[n//2][n//2] = n ** 2 // 4 + 1

    return answer


print(solution(5, True))
print(solution(6, False))
print(solution(9, False))