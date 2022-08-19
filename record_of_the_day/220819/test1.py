import heapq

def solution(region, num, info):
    answer = [-1 for _ in range(len(info))]
    new_info = []
    region_heap = []
    another_heap = []
    winner = 1
    num = min(num, len(info))

    for i in range(len(info)):
        new_info.append([i, info[i][0], (info[i][1] + 1) * 2 + (info[i][2] + 2) + (info[i][3] + 1) * 5])

    for i in range(len(new_info)):
        if new_info[i][1] == region:
            heapq.heappush(region_heap, (-new_info[i][2], new_info[i]))
        else:
            heapq.heappush(another_heap, (-new_info[i][2], new_info[i]))

    while winner <= num:
        if region_heap:
            infomation = heapq.heappop(region_heap)[1]
            answer[infomation[0]] = winner
        else:
            infomation = heapq.heappop(another_heap)[1]
            answer[infomation[0]] = winner
        winner += 1
    
    return answer


print(solution(2, 4, [[1,0,2,1],[2,6,5,2],[3,10,2,4],[1,1,5,6],[2,7,10,2],[3,8,6,3]]))