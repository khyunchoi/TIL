from math import ceil

def solution(n, times):
    answer = 0
    result_list = [float('inf') for _ in range(n+1)]
    result_list[0], result_list[1] = 0, 0
    times = [0] + times

    for i in range(2, n+1):
        for j in range(ceil(i/2), i):
            result_list[i] = min(result_list[i], result_list[j] + times[i-j])
    
    answer = result_list[-1]
    return answer


print(solution(4, [2, 3]))
print(solution(5, [2, 4, 5]))
print(solution(6, [1, 2, 3]))