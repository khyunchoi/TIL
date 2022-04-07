def solution(arr, brr):
    answer = 0
    tmp_arr = []

    tmp = 0
    for i in range(len(arr)):
        tmp += arr[i]
        tmp_arr.append(tmp)
    
    tmp_b = 0
    for i in range(len(brr)):
        tmp_b += brr[i]
        if tmp_arr[i] != tmp_b:
            answer += 1
            
    return answer

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))