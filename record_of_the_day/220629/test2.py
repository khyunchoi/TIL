def solution(A):
    bulb_list = [0 for _ in range(len(A))]

    result = 0
    for i in range(len(A)):
        for j in range(A[i]-1, len(A)):
            bulb_list[j] += 1
        
        if bulb_list[A[i]-1] == A[i]:
            result += 1
    
    return result


print(solution([2,1,3,5,4]))
print(solution([2,3,4,1,5]))
print(solution([1,3,4,2,5]))
print(solution([i+1 for i in range(10000)]))