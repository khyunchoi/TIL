import heapq
from math import ceil

def solution(fuel, powers, distances):
    answer = 0
    spaceship_list = []
    for i in range(len(powers)):
        tmp_time = (distances[i] / powers[i]) + 0.5
        spaceship_list.append([-tmp_time, tmp_time, 1])
    heapq.heapify(spaceship_list)
    
    fuel -= len(powers)
    while fuel:
        fuel -= 1

        spaceship = heapq.heappop(spaceship_list)
        now = (spaceship[1] - (spaceship[2] / 2)) * spaceship[2] / (spaceship[2] + 1) + ((spaceship[2] + 1) / 2)

        heapq.heappush(spaceship_list, [-now, now, spaceship[2]+1])

    answer = ceil(spaceship_list[0][1])
    return answer


print(solution(8, [20, 30], [750, 675]))
print(solution(19, 	[40, 30, 20, 10], [1000, 2000, 3000, 4000]))
print(solution(100, [100, 150], [1, 1000000]))
print(solution(5, [1, 2, 3, 4, 5], [50, 40, 30, 20, 10]))