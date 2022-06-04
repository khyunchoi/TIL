def solution(queue1, queue2):
    answer = -1
    result_list = []
    total_list = queue1 + queue2
    total = sum(total_list)
    if total % 2:
        return -1
    
    part_sum = 0
    j = 0
    for i in range(len(total_list)):
        while part_sum < total // 2 and j < len(total_list):
            part_sum += total_list[j]
            j += 1
            
        if part_sum == total // 2:
            if i < len(queue1):
                if j-1 < len(queue1) - 1:
                    result_list.append((i*2) + ((j) - i) + len(queue2))
                else:
                    result_list.append(i + (j) - len(queue1))
            else:
                result_list.append((i-len(queue1))*2 + ((j) - i) + len(queue1))
        
        part_sum -= total_list[i]
        
    if result_list:
        answer = min(result_list)
    
    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))