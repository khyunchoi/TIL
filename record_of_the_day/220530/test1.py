def solution(survey, choices):
    answer = ''
    personality_dict = {
        'RT' : [0, 0],
        'CF' : [0, 0],
        'JM' : [0, 0],
        'AN' : [0, 0]
    }
    personality_dict_keys = ['RT', 'CF', 'JM', 'AN']

    for i in range(len(survey)):
        if survey[i] in personality_dict:
            if choices[i] < 4:
                personality_dict[survey[i]][0] += 4 - choices[i]
            else:
                personality_dict[survey[i]][1] += choices[i] - 4
        else:
            if choices[i] < 4:
                personality_dict[survey[i][::-1]][1] += 4 - choices[i]
            else:
                personality_dict[survey[i][::-1]][0] += choices[i] - 4
            

    for key in personality_dict_keys:
        if personality_dict[key][0] < personality_dict[key][1]:
            answer += key[1]
        else:
            answer += key[0]

    return answer




print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))