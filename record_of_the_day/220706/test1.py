def solution(v, a, b):
    answer = 0

    flag = 1
    while flag:
        max_truck = 0
        max_truck_idx = 0
        for i in range(len(v)):
            if max_truck <= v[i]:
                max_truck = v[i]
                max_truck_idx = i
            v[i] -= b
            if v[i] < b:
                flag = 0
        v[max_truck_idx] -= (a - b)
        if v[max_truck_idx] < 0:
            break
        answer += 1

    return answer

print(solution([4,5,5],2,1))
print(solution([4,4,3],2,1))