def solution(logs):
    answer = []
    user_set = set()
    problem_dict = dict()
    logs = list(set(logs))
    
    for log in logs:
        user, problem = log.split()
        user_set.add(user)

        if problem in problem_dict:
            problem_dict[problem] += 1
        else:
            problem_dict[problem] = 1
    
    for problem, cnt in problem_dict.items():
        if len(user_set)/2 <= cnt:
            answer.append(problem)

    answer.sort()

    return answer


print(solution(["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]))
print(solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]))
print(solution(["kate sqrt"]))