from itertools import permutations
from copy import deepcopy

def solution(expression):
    answer = 0
    answer_list = []
    num_list = []
    temp_num_list = []
    calc_list = []
    temp_calc_list = []
    operator_list = ['+', '-', '*']
    permu_list = list(permutations([0, 1, 2], 3))

    for i in range(len(expression)-1, -1, -1):
        if not expression[i].isdigit():
            num_list.append(int(expression[i+1:]))
            calc_list.append(expression[i])
            expression = expression[:i]
    num_list.append(int(expression))
    num_list.reverse()
    calc_list.reverse()

    for permu in permu_list:
        temp_num_list, temp_calc_list = deepcopy(num_list), deepcopy(calc_list)
        for i in range(len(permu)):
            while operator_list[permu[i]] in temp_calc_list:
                idx = temp_calc_list.index(operator_list[permu[i]])
                temp_calc_list.pop(idx)

                if permu[i] == 0:
                    temp_num_list[idx] = temp_num_list[idx] + temp_num_list[idx+1]
                elif permu[i] == 1:
                    temp_num_list[idx] = temp_num_list[idx] - temp_num_list[idx+1]
                else:
                    temp_num_list[idx] = temp_num_list[idx] * temp_num_list[idx+1]
                temp_num_list.pop(idx+1)
        
        answer_list.append(abs(temp_num_list[0]))

    answer = max(answer_list)

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))