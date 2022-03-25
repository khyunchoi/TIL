import math

def solution(width, height, diagonals):
    answer = 0
    

    def combination(n, c):
        return math.factorial(n) // (math.factorial(c) * math.factorial(n-c))


    for x, y in diagonals:
        a = x
        b = y - 1
        n = a + b
        c = min(a, b)

        tmp1 = combination(n, c)

        a = width - x + 1
        b = height - y
        n = a + b
        c = min(a, b)

        tmp2 = combination(n, c)

        a = x - 1
        b = y
        n = a + b
        c = min(a, b)

        tmp3 = combination(n, c)

        a = width - x
        b = height - y + 1
        n = a + b
        c = min(a, b)

        tmp4 = combination(n, c)

        answer += (tmp1 * tmp2 + tmp3 * tmp4) % 10000019

    return answer

print(solution(2, 2, [[1,1],[2,2]]))
print(solution(51, 37, [[17,19]]))