import heapq

heap_list = []

heapq.heappush(heap_list, (1, -3, 3))
heapq.heappush(heap_list, (1, -4, 4))
heapq.heappush(heap_list, (1, -2, 2))
heapq.heappush(heap_list, (1, -1, 1))

print(heapq.heappop(heap_list)[2])
print(heapq.heappop(heap_list)[2])
print(heapq.heappop(heap_list)[2])
print(heapq.heappop(heap_list)[2])