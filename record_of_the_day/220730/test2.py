def solution(a, b, duration, distance):
    answer_list = []
    early = abs(a[0] - b[0])
    for i in range(early, -1, -1):
        early = i
        together = distance - early
        answer = min(a[0], b[0]) + early + (together + 1) // 2
        goodbye = answer + duration

        if (together) % 2:
            if a[1] - answer >= b[1] - answer:
                if a[0] >= b[0]:
                    if goodbye + (together + 1) // 2 > a[1] or goodbye + early + (together) // 2 > b[1]:
                        answer = -1
                else:
                    if goodbye + early + (together + 1) // 2 > a[1] or goodbye + (together) // 2 > b[1]:
                        answer = -1
            else:
                if a[0] >= b[0]:
                    if goodbye + (together) // 2 > a[1] or goodbye + early + (together + 1) // 2 > b[1]:
                        answer = -1
                else:
                    if goodbye + early + (together) // 2 > a[1] or goodbye + (together + 1) // 2 > b[1]:
                        answer = -1
        else:
            if a[0] >= b[0]:
                if goodbye + together // 2 > a[1] or goodbye + early + together // 2 > b[1]:
                    answer = -1
            else:
                if goodbye + early + together // 2 > a[1] or goodbye + together // 2 > b[1]:
                    answer = -1

        answer_list.append(answer)
    
    return min(answer_list)


print(solution([1, 6], [3, 5], 1, 2))
print(solution([1, 6], [2, 5], 1, 3))
print(solution([1, 4], [1, 4], 1, 2))
print(solution([1, 50], [51, 100], 100, 100))