from itertools import combinations, permutations
from copy import deepcopy

def solution(a, b, m):
    answer = float('inf')
    arr = [i for i in range(1, len(a)+2)]
    combi_arr = list(combinations(arr, 2))
    m_permu_arr = list(permutations(combi_arr, m))

    for a_element in a:
        if a_element[0] > a_element[1]:
            a_element[0], a_element[1] = a_element[1], a_element[0]

    for permu in m_permu_arr:
        tmp_b = deepcopy(b)
        for per in permu:
            x, y = per
            for b_element in tmp_b:
                if b_element[0] == x:
                    b_element[0] = y
                elif b_element[0] == y:
                    b_element[0] = x

                if b_element[1] == x:
                    b_element[1] = y
                elif b_element[1] == y:
                    b_element[1] = x

        for b_element in tmp_b:
            if b_element[0] > b_element[1]:
                b_element[0], b_element[1] = b_element[1], b_element[0]

        tmp_result = set()
        for a_element in a:
            tmp_result.add(tuple(a_element))
        for b_element in tmp_b:
            tmp_result.add(tuple(b_element))
        
        answer = min(answer, len(tmp_result) - len(a))

    return answer




print(solution([[1, 2], [2, 3]], [[1, 3], [3, 2]], 1))
print(solution([[1, 2], [3, 1], [2, 4], [3, 5]], [[2, 1], [4, 1], [2, 5], [3, 2]], 1))
print(solution([[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]], [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]], 2))