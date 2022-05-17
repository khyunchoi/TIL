import heapq

def solution(A):
    bulb_list = []
    heap_list = []

    result = 0
    for i in range(len(A)):
        if A[i]-1 == len(bulb_list):
            bulb_list.append(A[i])
            result += 1
        else:
            heapq.heappush(heap_list, A[i])
        
        while heap_list and heap_list[0]-1 == len(bulb_list):
            bulb_list.append(heapq.heappop(heap_list))
    
    return result


print(solution([2,1,3,5,4]))
print(solution([2,3,4,1,5]))
print(solution([1,3,4,2,5]))
print(solution([i for i in range(51, 0, -1)] + [i for i in range(52, 101)]))