from itertools import combinations

def solution(weight):
    answer = []
    tmp_answer = []


    def dfs(depth, part_sum):
        if part_sum > weight_goal:
            return

        if part_sum == weight_goal:
            tmp_answer.append([part_sum, len(tmp_weight[j])])
            return

        for x in range(depth, len(tmp_weight[j])):
            dfs(x+1, part_sum + tmp_weight[j][x])


    for i in range(len(weight), 1, -1):
        if tmp_answer:
            break

        tmp_weight = list(combinations(weight, i))

        for j in range(len(tmp_weight)):
            weight_sum = sum(tmp_weight[j])
            if weight_sum % 2:
                pass
            weight_goal = weight_sum // 2

            dfs(0, 0)

    tmp_answer.sort(reverse=True)
    answer.append(tmp_answer[0][1])
    answer.append(tmp_answer[0][0])
    return answer

def solution(weight):
    answer = []
    tmp_answer = []

    for i in range(len(weight), 1, -1):
        if tmp_answer:
            break

        tmp_weight = list(combinations(weight, i))

        for j in range(len(tmp_weight)):
            weight_sum = sum(tmp_weight[j])
            if weight_sum % 2:
                pass
            weight_goal = weight_sum // 2

            for k in range(len(tmp_weight[j]), 1, -1):
                tmp_tmp_weight = list(combinations([x for x in range(len(tmp_weight[j]))], k))

                for idx_list in tmp_tmp_weight:
                    part_sum = 0
                    for idx in idx_list:
                        part_sum += tmp_weight[j][idx]

                    if part_sum == weight_goal:
                        tmp_answer.append([part_sum, len(tmp_weight[j])])

    tmp_answer.sort(reverse=True)
    answer.append(tmp_answer[0][1])
    answer.append(tmp_answer[0][0])
    return answer