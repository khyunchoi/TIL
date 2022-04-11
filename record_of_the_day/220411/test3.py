def solution(tstring, variables):
    answer = ''
    dictionary = dict()
    original_dictionary = dict()
    cycle_key = []
    # tstring_list = tstring.split()

    for variable in variables:
        dictionary[variable[0]] = variable[1]
        original_dictionary[variable[0]] = variable[1]

    for key, value in dictionary.items():
        cnt = 0
        while value[0] == "{" and value[1:len(value)-1] in dictionary:
            if cnt > len(variables):
                dictionary[key] = original_dictionary[key]
                cycle_key.append(key)
                break

            tmp = value[1:len(value)-1]
            if tmp in dictionary:
                dictionary[key] = dictionary[tmp]
                value = dictionary[tmp]
            cnt += 1
    
    count = 0
    while count < len(tstring):
        if tstring[count] == "{":
            for j in range(count, len(tstring)):
                if tstring[j] == "}":
                    tmp = tstring[count+1:j]
                    if tmp not in cycle_key and tmp in dictionary:
                        answer += dictionary[tmp]
                    else:
                        answer += tstring[count:j+1]
                    count += len(tmp) + 2
                    break
        else:
            answer += tstring[count]
            count += 1

    # for i in range(len(tstring_list)):
    #     if tstring_list[i][0] == "{":
    #         tmp = tstring_list[i][1:len(tstring_list[i])-1]
    #         if tmp not in cycle_key and tmp in dictionary:
    #             tstring_list[i] = dictionary[tmp]

    # for tstr in tstring_list:
    #     answer += tstr + " "
    # answer = answer.strip()

    return answer

print(solution("this is {template} {template} is {state}", [["template", "string"], ["state", "changed"]]))
print(solution("this is {template} {template} is {state}", [["template", "string"], ["state", "{template}"]]))
print(solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{template}"]]))
print(solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{templates}"]]))
print(solution("{a} {b} {c} {d} {i}", [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))