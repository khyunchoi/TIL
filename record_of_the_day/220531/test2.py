def solution(queue1, queue2):
    answer = -1
    result_list = []
    total_list = queue1 + queue2
    total = sum(total_list)
    if total % 2:
        return -1
    
    for i in range(1, len(total_list)):
        part_sum = sum(total_list[:i])
        if part_sum == total // 2:
            end_idx = i-1
            if end_idx < len(queue1) - 1:
                result_list.append((end_idx+1) + len(queue2))
            elif end_idx == len(queue1) - 1:
                return 0
            else:
                result_list.append((end_idx+1) - len(queue1))
        for j in range(len(total_list)-i):
            part_sum = part_sum - total_list[j] + total_list[j+i]
            if part_sum == total // 2:
                start_idx = j+1
                end_idx = j+i
                if start_idx < len(queue1):
                    if end_idx < len(queue1) - 1:
                        result_list.append((start_idx*2) + ((end_idx+1) - start_idx) + len(queue2))
                    else:
                        result_list.append(start_idx + (end_idx+1) - len(queue1))
                else:
                    result_list.append((start_idx-len(queue1))*2 + ((end_idx+1) - start_idx) + len(queue1))
    
    if result_list:
        answer = min(result_list)

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))