def solution(grade):
    answer = 0

    min_val = float('inf')
    for i in range(len(grade)-1, -1, -1):
        min_val = min(min_val, grade[i])
        if grade[i] > min_val:
            answer += grade[i] - min_val

    return answer


print(solution([2,1,3]))
print(solution([1,2,3]))
print(solution([3,2,3,6,4,5]))