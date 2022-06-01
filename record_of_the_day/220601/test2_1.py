def solution(queue1, queue2):
    answer = -1
    result_list = []
    total_list = queue1 + queue2
    total = sum(total_list)
    if total % 2:
        return -1
    
    for i in range(len(total_list)):
        part_sum = 0
        for j in range(i, len(total_list)):
            part_sum += total_list[j]

            if part_sum > total // 2:
                break

            if part_sum == total // 2:
                if i == 0:
                    if j < len(queue1) - 1:
                        result_list.append((j+1) + len(queue2))
                    elif j == len(queue1) - 1:
                        return 0
                    else:
                        result_list.append((j+1) - len(queue1))
                else:
                    if i < len(queue1):
                        if j < len(queue1) - 1:
                            result_list.append((i*2) + ((j+1) - i) + len(queue2))
                        else:
                            result_list.append(i + (j+1) - len(queue1))
                    else:
                        result_list.append((i-len(queue1))*2 + ((j+1) - i) + len(queue1))

    
    if result_list:
        answer = min(result_list)

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))