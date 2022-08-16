def solution(call):
    answer = ''
    alpha_dict = dict()

    for alpha in call:
        alpha = alpha.lower()
        if alpha not in alpha_dict:
            alpha_dict[alpha] = 1
        else:
            alpha_dict[alpha] += 1
    
    max_value = 0
    for value in alpha_dict.values():
        max_value = max(max_value, value)
    
    for alpha in call:
        if alpha_dict[alpha.lower()] != max_value:
            answer += alpha

    return answer


print(solution("abcabcdefabc"))
print(solution("abxdeydeabz"))
print(solution("abcabca"))
print(solution("ABCabcA"))